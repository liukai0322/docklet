#!/usr/bin/python3

from flask import Flask, request, session, render_template, redirect, send_from_directory, make_response, url_for
from authenticate.auth import login_required, administration_required,activated_required
from authenticate.login import loginView, logoutView, iaaa_authView, pkuloginView
from authenticate.register import registerView
from dashboard.dashboard import dashboardView
from monitor.monitor import *
from user.userlist import userlistView, useraddView, usermodifyView, groupaddView, userdataView, userqueryView
from user.userinfo import userinfoView
from user.userActivate import userActivateView
from user.grouplist import grouplistView, groupqueryView, groupdetailView, groupmodifyView
from functools import wraps
from dockletreq.dockletrequest import dockletRequest
from cluster.cluster import *
import json
from jupytercookie import cookie_tool
import os
import getopt

import sys, inspect
this_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
src_folder = os.path.realpath(os.path.abspath(os.path.join(this_folder,"..", "src")))
doc_folder = os.path.realpath(os.path.abspath(os.path.join(this_folder,"..", "doc", "userguide","_book")))
if src_folder not in sys.path:
    sys.path.insert(0, src_folder)

from log import initlogging
initlogging("docklet-web")
from log import logger
import env

app = Flask(__name__)



@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/login/", methods=['GET', 'POST'])
def login():
    return loginView.as_view()

@app.route("/iaaa_auth/", methods=['GET'])
def iaaa_auth():
    return iaaa_authView.as_view()

@app.route("/pkulogin/", methods=['GET'])
def pkulogin():
    return pkuloginView.as_view()

@app.route("/logout/", methods=["GET"])
@login_required
def logout():
    return logoutView.as_view()

@app.route("/register/", methods=['GET', 'POST'])
@administration_required
#now forbidden,only used by SEI & PKU Staffs and students.
#can be used by admin for testing
def register():
    return registerView.as_view()



@app.route("/activate/", methods=['GET', 'POST'])
@login_required
def activate():
    return userActivateView.as_view()

@app.route("/dashboard/", methods=['GET'])
@login_required
def dashboard():
    return dashboardView.as_view()

@app.route("/dashboard_guest/", methods=['GET'])
def dashboard_guest():
    resp = make_response(dashboard_guestView.as_view())
    resp.set_cookie('guest-cookie', cookie_tool.generate_cookie('guest', app.secret_key))
    return resp

@app.route("/document/", methods=['GET'])
def redirect_dochome():
    return redirect("/document/index.html")

@app.route("/document/<path:path>", methods=['GET'])
def help_info(path):
    return send_from_directory(doc_folder, path)


@app.route("/config/", methods=['GET'])
@login_required
def config():
    return configView.as_view()


@app.route("/workspace/create/", methods=['GET'])
@activated_required
def addCluster():
    return addClusterView.as_view()

@app.route("/workspace/list/", methods=['GET'])
@login_required
def listCluster():
    return listClusterView.as_view()

@app.route("/workspace/add/", methods=['POST'])
@login_required
def createCluster():
    createClusterView.clustername = request.form["clusterName"]
    createClusterView.image = request.form["image"]
    createClusterView.onenode = request.form.getlist("onenode")
    createClusterView.multinodes = request.form.getlist("multinodes")
    return createClusterView.as_view()

@app.route("/workspace/scaleout/<clustername>/", methods=['POST'])
@login_required
def scaleout(clustername):
    scaleoutView.image = request.form["image"]
    scaleoutView.clustername = clustername
    scaleoutView.extensive = request.form.getlist("extensive")
    scaleoutView.onenode = request.form.getlist("onenode")
    return scaleoutView.as_view()

@app.route("/workspace/scalein/<clustername>/<containername>/", methods=['GET'])
@login_required
def scalein(clustername,containername):
    scaleinView.clustername = clustername
    scaleinView.containername = containername
    return scaleinView.as_view()

@app.route("/workspace/start/<clustername>/", methods=['GET'])
@login_required
def startClustet(clustername):
    startClusterView.clustername = clustername
    return startClusterView.as_view()

@app.route("/workspace/stop/<clustername>/", methods=['GET'])
@login_required
def stopClustet(clustername):
    stopClusterView.clustername = clustername
    return stopClusterView.as_view()

@app.route("/workspace/delete/<clustername>/", methods=['GET'])
@login_required
def deleteClustet(clustername):
    deleteClusterView.clustername = clustername
    return deleteClusterView.as_view()

@app.route("/workspace/detail/<clustername>/", methods=['GET'])
@login_required
def detailCluster(clustername):
    detailClusterView.clustername = clustername
    return detailClusterView.as_view()

@app.route("/workspace/flush/<clustername>/<containername>/", methods=['GET'])
@login_required
def flushCluster(clustername,containername):
    flushClusterView.clustername = clustername
    flushClusterView.containername = containername
    return flushClusterView.as_view()

@app.route("/workspace/save/<clustername>/<containername>/", methods=['POST'])
@login_required
def saveImage(clustername,containername):
    saveImageView.clustername = clustername
    saveImageView.containername = containername
    saveImageView.isforce = "false"
    saveImageView.imagename = request.form['ImageName']
    saveImageView.description = request.form['description']
    return saveImageView.as_view()

@app.route("/workspace/save/<clustername>/<containername>/force/", methods=['POST'])
@login_required
def saveImage_force(clustername,containername):
    saveImageView.clustername = clustername
    saveImageView.containername = containername
    saveImageView.isforce = "true"
    saveImageView.imagename = request.form['ImageName']
    saveImageView.description = request.form['description']
    return saveImageView.as_view()

@app.route("/image/description/<image>/", methods=['GET'])
@login_required
def descriptionImage(image):
    descriptionImageView.image = image
    return descriptionImageView.as_view()

@app.route("/image/share/<image>/", methods=['GET'])
@login_required
def shareImage(image):
    shareImageView.image = image
    return shareImageView.as_view()

@app.route("/image/unshare/<image>/", methods=['GET'])
@login_required
def unshareImage(image):
    unshareImageView.image = image
    return unshareImageView.as_view()

@app.route("/image/delete/<image>/", methods=['GET'])
@login_required
def deleteImage(image):
    deleteImageView.image = image
    return deleteImageView.as_view()

@app.route("/hosts/", methods=['GET'])
@administration_required
def monitorRealAll():
    return monitorRealAllView.as_view()

@app.route("/hosts/<com_ip>/", methods=['GET'])
@administration_required
def monitorReal(com_ip):
    monitorRealView.com_ip = com_ip
    return monitorRealView.as_view()

@app.route("/hosts/<com_ip>/containers/", methods=['GET'])
@administration_required
def monitorRealConAll(com_ip):
    monitorRealConAllView.com_ip = com_ip
    return monitorRealConAllView.as_view()

@app.route("/vclusters/", methods=['GET'])
@login_required
def monitor():
    return monitorView.as_view()

@app.route("/vclusters/<vcluster_name>/<node_name>/", methods=['GET'])
@login_required
def monitorNode(vcluster_name,node_name):
    monitorNodeView.node_name = node_name
    return monitorNodeView.as_view()

@app.route("/monitor/real/<comid>/<infotype>", methods=['POST'])
@app.route("/monitor/node/<comid>/<infotype>", methods=['POST'])
@login_required
def monitor_request(comid,infotype):
    data = {
        "user": session['username']
    }
    result = dockletRequest.post(request.path, data)
    return json.dumps(result)

@app.route("/monitor/User/", methods=['GET'])
@administration_required
def monitorUserAll():
    return monitorUserAllView.as_view()




@app.route("/user/list/", methods=['GET', 'POST'])
@administration_required
def userlist():
    return userlistView.as_view()

@app.route("/group/list/", methods=['POST'])
@administration_required
def grouplist():
    return grouplistView.as_view()

@app.route("/group/detail/", methods=['POST'])
@administration_required
def groupdetail():
    return groupdetailView.as_view()

@app.route("/group/query/", methods=['POST'])
@administration_required
def groupquery():
    return groupqueryView.as_view()

@app.route("/group/modify/", methods=['POST'])
@administration_required
def groupmodify():
    return groupmodifyView.as_view()

@app.route("/user/data/", methods=['GET', 'POST'])
@administration_required
def userdata():
    return userdataView.as_view()

@app.route("/user/add/", methods=['POST'])
@administration_required
def useradd():
    return useraddView.as_view()

@app.route("/user/modify/", methods=['POST'])
@administration_required
def usermodify():
    return usermodifyView.as_view()

@app.route("/group/add/", methods=['POST'])
@administration_required
def groupadd():
    return groupaddView.as_view()

@app.route("/user/info/", methods=['GET', 'POST'])
@login_required
def userinfo():
    return userinfoView.as_view()

@app.route("/user/query/", methods=['GET', 'POST'])
@administration_required
def userquery():
    return userqueryView.as_view()

@app.route('/index/', methods=['GET'])
def jupyter_control():
    return redirect('/dashboard/')

# for download basefs.tar.bz
@app.route('/download/basefs', methods=['GET'])
def download():
    return send_from_directory(app.runpath+'/../__temp', 'basefs.tar.bz', as_attachment=True)

# jupyter auth APIs
@app.route('/jupyter/', methods=['GET'])
def jupyter_prefix():
    path = request.args.get('next')
    if path == None:
        return redirect('/login/')
    return redirect('/login/'+'?next='+path)

@app.route('/jupyter/home/', methods=['GET'])
def jupyter_home():
    return redirect('/dashboard/')

@app.route('/jupyter/login/', methods=['GET', 'POST'])
def jupyter_login():
    return redirect('/login/')

@app.route('/jupyter/logout/', methods=['GET'])
def jupyter_logout():
    return redirect('/logout/')

@app.route('/jupyter/authorizations/cookie/<cookie_name>/<cookie_content>/', methods=['GET'])
def jupyter_auth(cookie_name, cookie_content):
    username = cookie_tool.parse_cookie(cookie_content, app.secret_key)
    if username == None:
        resp = make_response('cookie auth failed')
        resp.status_code = 404
        return resp
    return json.dumps({'name': username})

@app.route('/service/list/', methods=['POST'])
def service_list():
    imagename = request.form["imagename"]
    username = request.form["username"]
    isshared = request.form["isshared"]
    data = {"imagename":imagename, "username":username, "isshared":isshared}
    result = dockletRequest.post("/service/list/", data)
    if result:
        logger.info ('service list result : %s' % result)
        return json.dumps(result)

@app.route('/service/list2/', methods=['POST'])
def service_list2():
    imagename = request.form["imagename"]
    username = request.form["username"]
    isshared = request.form["isshared"]
    clustername = request.form["clustername"]
    data = {"imagename":imagename, "username":username, "isshared":isshared, "clustername":clustername}
    result = dockletRequest.post("/service/list2/", data)
    if result:
        logger.info ('service list2 result : %s' % result)
        return json.dumps(result)

@app.route('/service/list3/', methods=['POST'])
def service_list3():
    clustername = request.form['clustername']
    containername = request.form['containername']
    data = {"clustername":clustername, "containername":containername}
    result = dockletRequest.post("/service/list3/", data)
    if result:
        logger.info ('service list3 result : %s' % result)
        return json.dumps(result)

@app.route('/service/list4/', methods=['POST'])
def service_list4():
    imagename = request.form["imagename"]
    imageowner = request.form["imageowner"]
    imagetype = request.form["imagetype"]
    data = {"imagename":imagename, "imageowner":imageowner, "imagetype":imagetype}
    result = dockletRequest.post("/service/list4/", data)
    if result:
        logger.info ('service list4 result : %s' % result)
        return json.dumps(result)

@app.route('/service/config/', methods=['POST'])
def service_config():
    clustername = request.form['clustername']
    containername = request.form['containername']
    services = request.form['service']
    data = {"clustername":clustername, "containername":containername, "services":services}
    result = dockletRequest.post("/service/config/", data)
    if result:
        logger.info ('service list4 result : %s' % result)
        return json.dumps(result)

@app.route('/service/combine/', methods=['POST'])
def service_combine():
    imagename = request.form["imagename"]
    imageowner = request.form["imageowner"]
    imagetype = request.form["imagetype"]
    services = request.form["service"]
    data = {"imagename":imagename, "imageowner":imageowner, "imagetype":imagetype, "services":services}
    result = dockletRequest.post("/service/combine/", data)
    if result:
        logger.info ('service list4 result : %s' % result)
        return json.dumps(result)

@app.errorhandler(401)
def not_authorized(error):
    return render_template('error/401.html')

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error/500.html')

if __name__ == '__main__':
    '''
    to generate a secret_key

    from base64 import b64encode
    from os import urandom

    secret_key = urandom(24)
    secret_key = b64encode(secret_key).decode('utf-8')

    '''
    app.secret_key = 'DrjgnIwcbla+KxF4yWpOXZu4s+HpJnwb'
    os.environ['APP_KEY'] = app.secret_key
    runcmd = sys.argv[0]
    app.runpath = runcmd.rsplit('/', 1)[0]

    webip = "0.0.0.0"
    webport = env.getenv("WEB_PORT")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:p:", ["ip=", "port="])
    except getopt.GetoptError:
        print ("%s -i ip -p port" % sys.argv[0])
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ip"):
            webip = arg
        elif opt in ("-p", "--port"):
            webport = int(arg)

    app.run(host = webip, port = webport, debug = True)
