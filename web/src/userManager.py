'''
userManager for Docklet
provide a class for managing users and usergroups in Docklet
Warning: in some early versions, "token" stand for the instance of class model.User
         now it stands for a string that can be parsed to get that instance.
         in all functions start with "@administration_required" or "@administration_or_self_required", "token" is the instance
Original author: Liu Peidong
'''

from model import db, User, UserGroup
from functools import wraps
import os, subprocess
import hashlib
from userDependence import pam
from base64 import b64encode
import os
from log import logger
import env
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime

e_mail_from_address = 'NoReply@internetware.org'

def administration_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if ( ('cur_user' in kwargs) == False):
            return {"success":'false', "reason":"Cannot get cur_user"}
        cur_user = kwargs['cur_user']
        if ((cur_user.user_group == 'admin') or (cur_user.user_group == 'root')):
            return func(*args, **kwargs)
        else:
            return {"success": 'false', "reason": 'Unauthorized Action'}

    return wrapper

def administration_or_self_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if ( (not ('cur_user' in kwargs)) or (not ('user' in kwargs))):
            return {"success":'false', "reason":"Cannot get cur_user or user"}
        cur_user = kwargs['cur_user']
        if ((cur_user.user_group == 'admin') or (cur_user.user_group == 'root') or (cur_user.username == user.username)):
            return func(*args, **kwargs)
        else:
            return {"success": 'false', "reason": 'Unauthorized Action'}

    return wrapper

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if ( ('cur_user' in kwargs) == False):
            return {"success":'false', "reason":"Cannot get cur_user"}
        return func(*args, **kwargs)

    return wrapper

def send_activated_email(to_address, username):
    #text = 'Dear '+ username + ':\n' + '  Your account in docklet has been activated'
    text = '<html><h4>Dear '+ username + ':</h4>'
    text += '''<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Your account in <a href='%s'>%s</a> has been activated</p>
               <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please enjoy !</p>
               <br/>
               <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Please No Reply !</p>
               <br/><br/>
               <p> Docklet Team, SEI, PKU</p>
            ''' % (env.getenv("PORTAL_URL"), env.getenv("PORTAL_URL"))
    text += '<p>'+  str(datetime.utcnow()) + '</p>'
    text += '</html>'
    subject = 'Docklet account activated'
    msg = MIMEMultipart()
    textmsg = MIMEText(text,'html','utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = e_mail_from_address
    msg['To'] = to_address
    msg.attach(textmsg)
    s = smtplib.SMTP()
    s.connect()
    s.sendmail(e_mail_from_address, to_address, msg.as_string())
    s.close()


class userManager:
    def __init__(self, username = 'root', password = None):
        '''
        Try to create the database when there is none
        initialize 'root' user and 'root' & 'primary' group
        '''
        try:
            User.query.all()
            UserGroup.query.all()
        except:
            db.create_all()
            root = UserGroup('root')
            db.session.add(root)
            db.session.commit()
            if password == None:
                #set a random password
                password = os.urandom(16)
                password = b64encode(password).decode('utf-8')
                fsdir = env.getenv('FS_PREFIX')
                f = open(fsdir + '/local/generated_password.txt', 'w')
                f.write("User=%s\nPass=%s\n"%(username, password))
                f.close()
            sys_admin = User(username, hashlib.sha512(password.encode('utf-8')).hexdigest())
            sys_admin.status = 'normal'
            sys_admin.nickname = 'root'
            sys_admin.description = 'Root_User'
            sys_admin.user_group = 'root'
            sys_admin.auth_method = 'local'
            db.session.add(sys_admin)
            path = env.getenv('DOCKLET_LIB')
            subprocess.call([path+"/userinit.sh", username])
            db.session.commit()
            admin = UserGroup('admin')
            primary = UserGroup('primary')
            db.session.add(admin)
            db.session.add(primary)
            db.session.commit()

    def auth_local(self, username, password):
        password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        user = User.query.filter_by(username = username).first()
        if (user == None):
            return {"success":'false', "reason": "User did not exist"}
        if (user.password != password):
            return {"success":'false', "reason": "Wrong password"}
        result = {
            "success": 'true',
            "data":{
                "username" : user.username,
                "avatar" : user.avatar,
                "nickname" : user.nickname,
                "description" : user.description,
                "status" : user.status,
                "group" : user.user_group,
                "token" : user.generate_auth_token(),
            }
        }
        return result

    def auth_pam(self, username, password):
        user = User.query.filter_by(username = username).first()
        pamresult = pam.authenticate(username, password)
        if (pamresult == False or user.auth_method != 'pam'):
            return {"success":'false', "reason": "User did not exist or Wrong password or PKU user exists"}
        if (user == None):
            newuser = self.newuser();
            newuser.username = username
            newuser.password = "no_password"
            newuser.nickname = username
            newuser.status = "init"
            newuser.user_group = "primary"
            newuser.auth_method = "pam"
            self.register(user = newuser)
            user = User.query.filter_by(username = username).first()
        result = {
            "success": 'true',
            "data":{
                "username" : user.username,
                "avatar" : user.avatar,
                "nickname" : user.nickname,
                "description" : user.description,
                "status" : user.status,
                "group" : user.user_group,
                "token" : user.generate_auth_token(),
            }
        }
        return result

    def auth_iaaa(self, form):
        import xml.etree.cElementTree as ET
        tree = ET.fromstring(form)
        username = tree[6].text
        user = User.query.filter_by(username = username).first()
        if (user != None and user.auth_method == 'iaaa'):
            result = {
                "success": 'true',
                "data":{
                    "username" : user.username,
                    "avatar" : user.avatar,
                    "nickname" : user.nickname,
                    "description" : user.description,
                    "status" : user.status,
                    "group" : user.user_group,
                    "token" : user.generate_auth_token(),
                }
            }
            return result
        if (user != None and user.auth_method != 'iaaa'):
            result = {'success': 'false', 'reason': 'other kinds of account already exists'}
            return result
        #user == None , register an account for PKU user
        truename = tree[1].text
        department = tree[11].text
        newuser = self.newuser();
        newuser.username = username
        newuser.password = "no_password"
        newuser.nickname = truename
        newuser.truename = truename
        newuser.student_number = username
        newuser.status = "init"
        newuser.user_group = "primary"
        newuser.auth_method = "iaaa"
        newuser.department = department
        self.register(user = newuser)
        user = User.query.filter_by(username = username).first()
        result = {
            "success": 'true',
            "data":{
                "username" : user.username,
                "avatar" : user.avatar,
                "nickname" : user.nickname,
                "description" : user.description,
                "status" : user.status,
                "group" : user.user_group,
                "token" : user.generate_auth_token(),
            }
        }
        return result


    def auth(self, username, password):
        '''
        authenticate a user by username & password
        return a token as well as some user information
        '''
        user = User.query.filter_by(username = username).first()
        if (user == None or user.auth_method =='pam'):
            return self.auth_pam(username, password)
        elif (user.auth_method == 'local'):
            return self.auth_local(username, password)

    def auth_token(self, token):
        '''
        authenticate a user by a token
        when succeeded, return the database iterator
        otherwise return None
        '''
        user = User.verify_auth_token(token)
        return user

    @administration_required
    def query(*args, **kwargs):
        '''
        Usage: query(username = 'xxx', cur_user = token_from_auth)
            || query(ID = a_integer, cur_user = token_from_auth)
        Provide information about one user that administrators need to use
        '''
        if ( 'ID' in kwargs):
            user = User.query.filter_by(id = kwargs['ID']).first()
            if (user == None):
                return {"success":False, "reason":"User does not exist"}
            result = {
                "success":'true',
                "data":{
                    "username" : user.username,
                    "password" : user.password,
                    "avatar" : user.avatar,
                    "nickname" : user.nickname,
                    "description" : user.description,
                    "status" : user.status,
                    "e_mail" : user.e_mail,
                    "student_number": user.student_number,
                    "department" : user.department,
                    "truename" : user.truename,
                    "tel" : user.tel,
                    "register_date" : "%s"%(user.register_date),
                    "group" : user.user_group,
                },
                "token": user
            }
            return result

        if ( 'username' not in kwargs):
            return {"success":'false', "reason":"Cannot get 'username'"}
        username = kwargs['username']
        user = User.query.filter_by(username = username).first()
        if (user == None):
            return {"success":'false', "reason":"User does not exist"}
        result = {
            "success": 'true',
            "data":{
                "username" : user.username,
                "password" : user.password,
                "avatar" : user.avatar,
                "nickname" : user.nickname,
                "description" : user.description,
                "status" : user.status,
                "e_mail" : user.e_mail,
                "student_number": user.student_number,
                "department" : user.department,
                "truename" : user.truename,
                "tel" : user.tel,
                "register_date" : "%s"%(user.register_date),
                "group" : user.user_group,
            },
            "token": user
        }
        return result

    @token_required
    def selfQuery(*args, **kwargs):
        '''
        Usage: selfQuery(cur_user = token_from_auth)
        List informantion for oneself
        '''
        user = kwargs['cur_user']
        result = {
            "success": 'true',
            "data":{
                "username" : user.username,
                "password" : user.password,
                "avatar" : user.avatar,
                "nickname" : user.nickname,
                "description" : user.description,
                "status" : user.status,
                "e_mail" : user.e_mail,
                "student_number": user.student_number,
                "department" : user.department,
                "truename" : user.truename,
                "tel" : user.tel,
                "register_date" : "%s"%(user.register_date),
                "group" : user.user_group,
            },
        }
        return result

    @token_required
    def selfModify(*args, **kwargs):
        '''
        Usage: selfModify(cur_user = token_from_auth, newValue = form)
        Modify informantion for oneself
        '''
        form = kwargs['newValue']
        name = form.getvalue('name', None)
        value = form.getvalue('value', None)
        if (name == None or value == None):
            result = {'success': 'false'}
            return result
        user = User.query.filter_by(username = kwargs['cur_user'].username).first()
        if (name == 'nickname'):
            user.nickname = value
        elif (name == 'description'):
            user.description = value
        elif (name == 'department'):
            user.department = value
        elif (name == 'e_mail'):
            user.e_mail = value
        elif (name == 'tel'):
            user.tel = value
        else:
            result = {'success': 'false'}
            return result
        db.session.commit()
        result = {'success': 'true'}
        return result


    @administration_required
    def userList(*args, **kwargs):
        '''
        Usage: list(cur_user = token_from_auth)
        List all users for an administrator
        '''
        alluser = User.query.all()
        result = {
            "success": 'true',
            "data":[]
        }
        for user in alluser:
            userinfo = [
                    user.id,
                    user.username,
                    user.truename,
                    user.e_mail,
                    user.tel,
                    "%s"%(user.register_date),
                    user.status,
                    user.user_group,
                    '',
            ]
            result["data"].append(userinfo)
        return result

    @administration_required
    def groupList(*args, **kwargs):
        '''
        Usage: list(cur_user = token_from_auth)
        List all groups for an administrator
        '''
        allgroup = UserGroup.query.all()
        result = {
            "success": 'true',
            "data":[]
        }
        for group in allgroup:
            groupinfo = [
                    group.id,
                    group.name,
                    group.cpu,
                    group.memory,
                    group.imageQuantity,
                    group.lifeCycle,
                    '',
            ]
            result["data"].append(groupinfo)
        return result

    @administration_required
    def groupQuery(*args, **kwargs):
        '''
        Usage: groupQuery(id = XXX, cur_user = token_from_auth)
        List a group for an administrator
        '''
        group = UserGroup.query.filter_by(id = kwargs['ID']).first()
        if (group == None):
            return {"success":False, "reason":"Group does not exist"}
        result = {
            "success":'true',
            "data":{
                "name" : group.name ,
                "cpu" : group.cpu ,
                "memory" : group.memory,
                "imageQuantity" : group.imageQuantity,
                "lifeCycle" : group.lifeCycle,
            }
        }
        return result

    @administration_required
    def groupListName(*args, **kwargs):
        '''
        Usage: grouplist(cur_user = token_from_auth)
        List all group names for an administrator
        '''
        groups = UserGroup.query.all()
        result = {
            "groups": [],
        }
        for group in groups:
            result["groups"].append(group.name)
        return result

    @administration_required
    def groupModify(*args, **kwargs):
        '''
        Usage: groupModify(newValue = dict_from_form, cur_user = token_from_auth)
        '''
        group_modify = UserGroup.query.filter_by(name = kwargs['newValue'].getvalue('groupname', None)).first()
        if (group_modify == None):
            return {"success":'false', "reason":"UserGroup does not exist"}
        form = kwargs['newValue']
        group_modify.cpu = form.getvalue('cpu', '')
        group_modify.memory = form.getvalue('memory', '')
        group_modify.imageQuantity = form.getvalue('image', '')
        group_modify.lifeCycle = form.getvalue('lifecycle', '')
        db.session.commit()
        return {"success":'true'}

    @administration_required
    def modify(*args, **kwargs):
        '''
        modify a user's information in database
        will send an e-mail when status is changed from 'applying' to 'normal'
        Usage: modify(newValue = dict_from_form, cur_user = token_from_auth)
        '''
        user_modify = User.query.filter_by(username = kwargs['newValue'].getvalue('username', None)).first()
        if (user_modify == None):

            return {"success":'false', "reason":"User does not exist"}

        #try:
        form = kwargs['newValue']
        user_modify.truename = form.getvalue('truename', '')
        user_modify.e_mail = form.getvalue('e_mail', '')
        user_modify.department = form.getvalue('department', '')
        user_modify.student_number = form.getvalue('student_number', '')
        user_modify.tel = form.getvalue('tel', '')
        user_modify.user_group = form.getvalue('group', '')
        user_modify.auth_method = form.getvalue('auth_method', '')
        if (user_modify.status == 'applying' and form.getvalue('status', '') == 'normal'):
            send_activated_email(user_modify.e_mail, user_modify.username)
        user_modify.status = form.getvalue('status', '')
        if (form.getvalue('Chpassword', '') == 'Yes'):
            new_password = form.getvalue('password','no_password')
            new_password = hashlib.sha512(new_password.encode('utf-8')).hexdigest()
            user_modify.password = new_password
            #self.chpassword(cur_user = user_modify, password = form.getvalue('password','no_password'))

        db.session.commit()
        return {"success":'true'}
        #except:
            #return {"success":'false', "reason":"Something happened"}

    @token_required
    def chpassword(*args, **kwargs):
        '''
        Usage: chpassword(cur_user = token_from_auth, password = 'your_password')
        '''
        cur_user.password = hashlib.sha512(kwargs['password'].encode('utf-8')).hexdigest()

    def newuser(*args, **kwargs):
        '''
        Usage : newuser()
        The only method to create a new user
        call this method first, modify the return value which is a database row instance,then call self.register()
        '''
        user_new = User('newuser', 'asdf1234')
        user_new.user_group = 'primary'
        user_new.avatar = 'default.png'
        return user_new

    def register(*args, **kwargs):
        '''
        Usage: register(user = modified_from_newuser())
        '''

        if (kwargs['user'].username == None or kwargs['user'].username == ''):
            return {"success":'false', "reason": "Empty username"}
        user_check = User.query.filter_by(username = kwargs['user'].username).first()
        if (user_check != None and user_check.status != "init"):
            #for the activating form
            return {"success":'false', "reason": "Unauthorized action"}
        if (user_check != None and (user_check.status == "init")):
            db.session.delete(user_check)
            db.session.commit()
        newuser = kwargs['user']
        newuser.password = hashlib.sha512(newuser.password.encode('utf-8')).hexdigest()
        db.session.add(kwargs['user'])
        db.session.commit()

        # if newuser status is normal, init some data for this user
        # now initialize for all kind of users
        #if newuser.status == 'normal':
        path = env.getenv('DOCKLET_LIB')
        subprocess.call([path+"/userinit.sh", newuser.username])
        return {"success":'true'}

    @administration_required
    def groupadd(*args, **kwargs):
        name = kwargs.get('name', None)
        if (name == None):
            return {"success":'false', "reason": "Empty group name"}
        group_new = UserGroup(name)
        db.session.add(group_new)
        db.session.commit()
        return {"success":'true'}

    def queryForDisplay(*args, **kwargs):
        '''
        Usage: queryForDisplay(user = token_from_auth)
        Provide information about one user that administrators need to use
        '''

        if ( 'user' not in kwargs):
            return {"success":'false', "reason":"Cannot get 'user'"}
        user = kwargs['user']
        if (user == None):
            return {"success":'false', "reason":"User does not exist"}
        result = {
            "success": 'true',
            "data":{
                "username" : user.username,
                "password" : user.password,
                "avatar" : user.avatar,
                "nickname" : user.nickname,
                "description" : user.description,
                "status" : user.status,
                "e_mail" : user.e_mail,
                "student_number": user.student_number,
                "department" : user.department,
                "truename" : user.truename,
                "tel" : user.tel,
                "register_date" : "%s"%(user.register_date),
                "group" : user.user_group,
                "auth_method": user.auth_method,
            }
        }
        return result

    def usermodify(rowID, columnID, newValue, cur_user):
        '''not used now'''
        user = um.query(ID = request.form["rowID"], cur_user = root).get('token',  None)
        result = um.modify(user = user, columnID = request.form["columnID"], newValue = request.form["newValue"], cur_user = root)
        return json.dumps(result)
