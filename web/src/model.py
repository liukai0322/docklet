#coding=utf-8
'''
2 tables: users, usergroup
User:
    id
    username
    password
    avatar
    nickname
    description
    status
    student_number
    department
    truename
    tel
    e_mail
    register_date
    user_group
    auth_method

Usergroup
    id
    name

Token expiration can be set in User.generate_auth_token
'''
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from base64 import b64encode, b64decode
import os

#this class from itsdangerous implements token<->user
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import JSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature

import env

fsdir = env.getenv('FS_PREFIX')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+fsdir+'/local/UserTable.db'
app.secret_key = 'TT+WldpsXkRYnnHyKrIYghYJfmjSxZT5'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(100))
    avatar = db.Column(db.String(30))
    nickname = db.Column(db.String(10))
    description = db.Column(db.String(15))
    status = db.Column(db.String(10))
    e_mail = db.Column(db.String(20))
    student_number = db.Column(db.String(20))
    department = db.Column(db.String(20))
    truename = db.Column(db.String(20))
    tel = db.Column(db.String(20))
    register_date = db.Column(db.String(10))
    user_group = db.Column(db.String(50))
    auth_method = db.Column(db.String(10))

    #可以改成关系型数据，目前为了修改方便只存组别名

    def __init__(self, username, password, avatar="default.png", nickname = "", description = "", status = "init",
                    e_mail = "" , student_number = "", department = "", truename = "", tel="", date = None, usergroup = "primary"
                , auth_method = "local"):
        # using sha512, length cannot be less than 6
        #if (len(password) <= 6):
        #    self = None
        #    return None
        self.username = username
        self.password = password
        self.avatar = avatar
        self.nickname = nickname
        self.description = description
        self.status = status
        self.e_mail = e_mail
        self.student_number = student_number
        self.department = department
        self.truename = truename
        self.tel = tel
        if (date != None):
            self.register_date = date
        else:
            self.register_date = datetime.utcnow()
        if (UserGroup.query.filter_by(name=usergroup).first() != None):
            self.user_group = usergroup
        else:
            self.user_group = "primary"
        self.auth_method = auth_method

    def __repr__(self):
        return '<User %r>' % self.username

    #token will expire after 3600s
    # replace token with no time expiration
    def generate_auth_token(self, expiration = 3600):
        s = Serializer(app.config['SECRET_KEY'])
        str = s.dumps({'id': self.id})
        return b64encode(str).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(b64decode(token))
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user


class UserGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cpu = db.Column(db.String(10))
    memory = db.Column(db.String(10))
    imageQuantity = db.Column(db.String(10))
    lifeCycle = db.Column(db.String(10))

    def __init__(self, name):
        self.name = name
        self.cpu = '2000'
        self.memory = '2000'
        self.imageQuantity = '10'
        self.lifeCycle = '24'

    def __repr__(self):
        return '<UserGroup %r>' % self.name
