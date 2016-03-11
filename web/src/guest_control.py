#!/usr/bin/python3

import os,time,subprocess
import proxytool
import env

class Guest(object):
    def __init__(self,vclusterMgr,nodemgr):
        self.libpath = env.getenv('DOCKLET_LIB')
        self.fspath = env.getenv('FS_PREFIX')
        self.lxcpath = "/var/lib/lxc"
        self.G_vclustermgr = vclusterMgr
        self.nodemgr = nodemgr

    def work(self):
        image = {}
        image['name'] = "base"
        image['type'] = "base"
        image['owner'] = "docklet"
        while len(self.nodemgr.get_rpcs()) < 1:
            time.sleep(10)
        if not os.path.isdir(self.fspath+"/global/users/guest"):
            subprocess.getoutput(self.libpath+"/userinit.sh guest")
        self.G_vclustermgr.create_cluster("guestspace", "guest", image)
        [infostatus, clusterinfo] = self.G_vclustermgr.get_clusterinfo("guestspace", "guest")
        target = 'http://' + clusterinfo['containers'][0]['ip'].split('/')[0]+":10000"
        while(True):
            [status, out] = proxytool.set_route('go/guest/guestspace',target)
            if status:
                break
            else:
                time.sleep(30)
        while True:
            self.G_vclustermgr.start_cluster("guestspace", "guest")
            time.sleep(3600)
            self.G_vclustermgr.stop_cluster("guestspace", "guest")
            fspath = self.fspath + "/global/local/volume/guest-1-0/upper/"
            subprocess.getoutput("(cd %s && rm -rf *)" % fspath)
