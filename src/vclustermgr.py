#!/usr/bin/python3

import os, random, json, sys, imagemgr, threading, servicemgr
import datetime

from log import logger
import env

##################################################
#                  VclusterMgr
# Description : VclusterMgr start/stop/manage virtual clusters
#
##################################################

class VclusterMgr(object):
    def __init__(self, nodemgr, networkmgr, etcdclient, addr, mode):
        self.mode = mode
        self.nodemgr = nodemgr
        self.imgmgr = imagemgr.ImageMgr()
        self.servmgr = servicemgr.ServiceMgr()
        self.networkmgr = networkmgr
        self.addr = addr
        self.etcd = etcdclient
        self.defaultsize = env.getenv("CLUSTER_SIZE")
        self.fspath = env.getenv("FS_PREFIX")

        logger.info ("vcluster start on %s" % (self.addr))
        if self.mode == 'new':
            logger.info ("starting in new mode on %s" % (self.addr))
            # check if all clusters data are deleted in httprest.py
            clean = True
            usersdir = self.fspath+"/global/users/"
            for user in os.listdir(usersdir):
                if len(os.listdir(usersdir+user+"/clusters")) > 0 or len(os.listdir(usersdir+user+"/hosts")) > 0:
                    clean = False
            if not clean:
                logger.error ("clusters files not clean, start failed")
                sys.exit(1)
        elif self.mode == "recovery":
            logger.info ("starting in recovery mode on %s" % (self.addr))
            self.recover_allclusters()
        else:
            logger.error ("not supported mode:%s" % self.mode)
            sys.exit(1)

    def recover_allclusters(self):
        logger.info("recovering all vclusters for all users...")
        usersdir = self.fspath+"/global/users/"
        for user in os.listdir(usersdir):
            for cluster in self.list_clusters(user)[1]:
                logger.info ("recovering cluster:%s for user:%s ..." % (cluster, user))
                self.recover_cluster(cluster, user)
        logger.info("recovered all vclusters for all users")

    def create_cluster(self, clustername, username, image, onenode=None, multinodes=None):
        if self.is_cluster(clustername, username):
            return [False, "cluster:%s already exists" % clustername]
        logger.info ('onenode : %s, multinodes : %s' % (onenode, multinodes))
        clustersize = self.defaultsize;
        [clustersize, service] = self.servmgr.create_service(username, clustername, image, onenode, multinodes)
        logger.info ("starting cluster %s with %d containers for %s" % (clustername, clustersize, username))
        workers = self.nodemgr.get_rpcs()
        if (len(workers) == 0):
            logger.warning ("no workers to start containers, start cluster failed")
            return [False, "no workers are running"]
        imagename = image['name']
        imageowner = image['owner']
        imagetype = image['type']
        #logger.info ("imagename : %s, imageowner : %s, imagetype : %s" % (imagename, imageowner, imagetype))
        # check user IP pool status, should be moved to user init later
        if not self.networkmgr.has_user(username):
            self.networkmgr.add_user(username, cidr=29)
        [status, result] = self.networkmgr.acquire_userips_cidr(username, clustersize)
        gateway = self.networkmgr.get_usergw(username)
        vlanid = self.networkmgr.get_uservlanid(username)
        logger.info ("create cluster with gateway : %s" % gateway)
        self.networkmgr.printpools()
        if not status:
            return [False, result]
        ips = result
        clusterid = self._acquire_id()
        clusterpath = self.fspath+"/global/users/"+username+"/clusters/"+clustername
        hostpath = self.fspath+"/global/users/"+username+"/hosts/"+str(clusterid)+".hosts"
        hosts = "127.0.0.1\tlocalhost\n"
        containers = []
        for i in range(0, clustersize):
            onework = workers[random.randint(0, len(workers)-1)]
            lxc_name = username + "-" + str(clusterid) + "-" + str(i)
            hostname = "host-"+str(i)
            logger.info ("create container with : name-%s, username-%s, clustername-%s, clusterid-%s, hostname-%s, ip-%s, gateway-%s, imagename-%s, imageowner-%s, imagetype-%s" % (lxc_name, username, clustername, str(clusterid), hostname, ips[i], gateway, imagename, imageowner, imagetype))
            onework.create_container(lxc_name, username, clustername, str(clusterid), hostname, ips[i], gateway, str(vlanid), imagename, imageowner, imagetype )
            logger.info("container create success")
            hosts = hosts + ips[i].split("/")[0] + "\t" + hostname + "\t" + hostname + "."+clustername + "\n"
            containers.append({ 'containername':lxc_name, 'hostname':hostname, 'ip':ips[i], 'host':self.nodemgr.rpc_to_ip(onework), 'image':image['name'], 'lastsave':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") })
        hostfile = open(hostpath, 'w')
        hostfile.write(hosts)
        hostfile.close()
        clusterfile = open(clusterpath, 'w')
        info = {'clusterid':clusterid, 'status':'stopped', 'size':clustersize, 'containers':containers, 'nextcid': clustersize, 'create_time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'start_time':"------" }
        info['services'] = service
        clusterfile.write(json.dumps(info))
        clusterfile.close()
        return [True, info]

    def scale_out_cluster(self,clustername,username,image,extensive,onenode):
        if not self.is_cluster(clustername,username):
            return [False, "cluster:%s not found" % clustername]
        workers = self.nodemgr.get_rpcs()
        if (len(workers) == 0):
            logger.warning("no workers to start containers, scale out failed")
            return [False, "no workers are running"]
        imagename = image['name']
        imageowner = image['owner']
        imagetype = image['type']
        [status, result] = self.networkmgr.acquire_userips_cidr(username)
        gateway = self.networkmgr.get_usergw(username)
        vlanid = self.networkmgr.get_uservlanid(username)
        self.networkmgr.printpools()
        if not status:
            return [False, result]
        ip = result[0]
        [status, clusterinfo] = self.get_clusterinfo(clustername,username)
        clusterid = clusterinfo['clusterid']
        clusterpath = self.fspath + "/global/users/" + username + "/clusters/" + clustername
        hostpath = self.fspath + "/global/users/" + username + "/hosts/" + str(clusterid) + ".hosts"
        cid = clusterinfo['nextcid']
        [newservices, cmd] = self.servmgr.scale_out(username, clustername, clusterinfo, cid, extensive, onenode, image)
        onework = workers[random.randint(0, len(workers)-1)]
        lxc_name = username + "-" + str(clusterid) + "-" + str(cid)
        hostname = "host-" + str(cid)
        onework.create_container(lxc_name, username, clustername, clusterid, hostname, ip, gateway, str(vlanid), imagename, imageowner, imagetype)
        if clusterinfo['status'] == "running":
            onework.start_container(lxc_name)
            onework.start_services(lxc_name, cmd, False)
        logger.info("scale out success")
        hostfile = open(hostpath, 'a')
        hostfile.write(ip.split("/")[0] + "\t" + hostname + "\t" + hostname + "." + clustername + "\n")
        hostfile.close()
        clusterinfo['nextcid'] = int(clusterinfo['nextcid']) + 1
        clusterinfo['size'] = int(clusterinfo['size']) + 1
        clusterinfo['services'] = newservices
        clusterinfo['containers'].append({'containername':lxc_name, 'hostname':hostname, 'ip':ip, 'host':self.nodemgr.rpc_to_ip(onework), 'image':image['name'], 'lastsave':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") })
        clusterfile = open(clusterpath, 'w')
        clusterfile.write(json.dumps(clusterinfo))
        clusterfile.close()
        return [True, clusterinfo]

    def flush_cluster(self,username,clustername,containername):
        begintime = datetime.datetime.now()
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return [False, "cluster not found"]
        containers = info['containers']
        imagetmp = username + "_tmp_docklet"
        for container in containers:
            if container['containername'] == containername:
                logger.info("container: %s found" % containername)
                onework = self.nodemgr.ip_to_rpc(container['host'])
                onework.create_image(username,imagetmp,containername)
                fimage = container['image']
                logger.info("image: %s created" % imagetmp)
                break
        else:
            logger.error("container: %s not found" % containername)
        threads = []
        for container in containers:
            if container['containername'] != containername:
                logger.info("container: %s now flush" % container['containername'])
                onework = self.nodemgr.ip_to_rpc(container['host'])
                #t = threading.Thread(target=onework.flush_container,args=(username,imagetmp,container['containername']))
                #threads.append(t)
                onework.flush_container(username,imagetmp,container['containername'])
                container['lastsave'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                container['image'] = fimage
                logger.info("thread for container: %s has been prepared" % container['containername'])
       # for t in threads:
       #     t.start()
       # for t in threads:
       #     t.join()
        clusterpath = self.fspath + "/global/users/" + username + "/clusters/" + clustername
        infofile = open(clusterpath,'w')
        infofile.write(json.dumps(info))
        infofile.close()
        self.imgmgr.removeImage(username,imagetmp)
        endtime = datetime.datetime.now()
        dtime = (endtime - begintime).seconds
        logger.info("flush spend %s seconds" % dtime)
        logger.info("flush success")


    def create_image(self,username,clustername,containername,imagename,description,isforce=False):
        [status, info] = self.get_clusterinfo(clustername,username)
        if not status:
            return [False, "cluster not found"]
        containers = info['containers']
        for container in containers:
            if container['containername'] == containername:
                logger.info("container: %s found" % containername)
                onework = self.nodemgr.ip_to_rpc(container['host'])
                res = onework.create_image(username,imagename,containername,description,isforce)
                container['lastsave'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                container['image'] = imagename
                break
        else:
            res = [False, "container not found"]
            logger.error("container: %s not found" % containername)
        clusterpath = self.fspath + "/global/users/" + username + "/clusters/" + clustername
        infofile = open(clusterpath, 'w')
        infofile.write(json.dumps(info))
        infofile.close()
        return res

    def delete_cluster(self, clustername, username):
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return [False, "cluster not found"]
        if info['status']=='running':
            return [False, "cluster is still running, you need to stop it and then delete"]
        ips = []
        for container in info['containers']:
            worker = self.nodemgr.ip_to_rpc(container['host'])
            worker.delete_container(container['containername'])
            ips.append(container['ip'])
        logger.info("delete vcluster and release vcluster ips")
        self.networkmgr.release_userips(username, ips)
        self.networkmgr.printpools()
        os.remove(self.fspath+"/global/users/"+username+"/clusters/"+clustername)
        os.remove(self.fspath+"/global/users/"+username+"/hosts/"+str(info['clusterid'])+".hosts")
        return [True, "cluster delete"]

    def scale_in_cluster(self, clustername, username, containername):
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return [False, "cluster not found"]
        new_containers = []
        for container in info['containers']:
            if container['containername'] == containername:
                worker = self.nodemgr.ip_to_rpc(container['host'])
                worker.delete_container(containername)
                self.networkmgr.release_userips(username, container['ip'])
                self.networkmgr.printpools()
            else:
                new_containers.append(container)
        info['containers'] = new_containers
        info['size'] -= 1
        cid = containername[containername.rindex("-")+1:]
        clusterid = info['clusterid']
        clusterpath = self.fspath + "/global/users/" + username + "/clusters/" + clustername
        hostpath = self.fspath + "/global/users/" + username + "/hosts/" + str(clusterid) + ".hosts"
        clusterfile = open(clusterpath, 'w')
        clusterfile.write(json.dumps(info))
        clusterfile.close()
        hostfile = open(hostpath, 'r')
        hostinfo = hostfile.readlines()
        hostfile.close()
        hostfile = open(hostpath, 'w')
        new_hostinfo = []
        new_hostinfo.append(hostinfo[0])
        for host in hostinfo[1:]:
            parts = host.split("\t")
            if parts[1][parts[1].rindex("-")+1:] == cid:
                pass
            else:
                new_hostinfo.append(host)
        hostfile.writelines(new_hostinfo)
        hostfile.close()
        return [True, info]


    def start_cluster(self, clustername, username):
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return [False, "cluster not found"]
        if info['status'] == 'running':
            return [False, "cluster is already running"]

        #prepare services
        services = self.servmgr.gen_servicecmd(clustername, username, info)

        #start containers and services
        i = 0
        for container in info['containers']:
            worker = self.nodemgr.ip_to_rpc(container['host'])
            worker.start_container(container['containername'])
            worker.start_services(container['containername'], services[i], i == 0)
            i = i + 1
        info['status']='running'
        info['start_time']=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        infofile = open(self.fspath+"/global/users/"+username+"/clusters/"+clustername, 'w')
        infofile.write(json.dumps(info))
        infofile.close()
        return [True, "start cluster"]

    def recover_cluster(self, clustername, username):
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return [False, "cluster not found"]
        if info['status'] == 'stopped':
            return [True, "cluster no need to start"]
        # TODO : need to check and recover gateway of this user
        # TODO : need to check and recover proxy of this cluster
        # recover containers of this cluster
        for container in info['containers']:
            worker = self.nodemgr.ip_to_rpc(container['host'])
            worker.recover_container(container['containername'])
        return [True, "start cluster"]


    # maybe here should use cluster id
    def stop_cluster(self, clustername, username):
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return [False, "cluster not found"]
        if info['status'] == 'stopped':
            return [False, 'cluster is already stopped']
        for container in info['containers']:
            worker = self.nodemgr.ip_to_rpc(container['host'])
            worker.stop_container(container['containername'])
        info['status']='stopped'
        info['start_time']="------"
        infofile = open(self.fspath+"/global/users/"+username+"/clusters/"+clustername, 'w')
        infofile.write(json.dumps(info))
        infofile.close()
        return [True, "start cluster"]

    def list_clusters(self, user):
        if not os.path.exists(self.fspath+"/global/users/"+user+"/clusters"):
            return [True, []]
        clusters = os.listdir(self.fspath+"/global/users/"+user+"/clusters")
        full_clusters = []
        for cluster in clusters:
            single_cluster = {}
            single_cluster['name'] = cluster
            [status, info] = self.get_clusterinfo(cluster,user)
            if info['status'] == 'running':
                single_cluster['status'] = 'running'
            else:
                single_cluster['status'] = 'stopping'
            full_clusters.append(single_cluster)
        return [True, clusters]

    def is_cluster(self, clustername, username):
        [status, clusters] = self.list_clusters(username)
        if clustername in clusters:
            return True
        else:
            return False

    # get id from name
    def get_clusterid(self, clustername, username):
        [status, info] = self.get_clusterinfo(clustername, username)
        if not status:
            return -1
        if 'clusterid' in info:
            return int(info['clusterid'])
        logger.error ("internal error: cluster:%s info file has no clusterid " % clustername)
        return -1

    def get_clusterinfo(self, clustername, username):
        clusterpath = self.fspath + "/global/users/" + username + "/clusters/" + clustername
        if not os.path.isfile(clusterpath):
            return [False, "cluster not found"]
        infofile = open(clusterpath, 'r')
        info = json.loads(infofile.read())
        return [True, info]

    # acquire cluster id from etcd
    def _acquire_id(self):
        clusterid = self.etcd.getkey("vcluster/nextid")[1]
        self.etcd.setkey("vcluster/nextid", str(int(clusterid)+1))
        return int(clusterid)
