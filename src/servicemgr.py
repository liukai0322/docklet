#!/usr/bin/python3

import os, json

from log import logger


class ServiceMgr():
    def sys_call(self, command):
        output = subprocess.getoutput(command).strip()
        return None if output == '' else output

    def sys_return(self,command):
        return_value = subprocess.call(command,shell=True)
        return return_value

    def load_file(self, fileurl):
        if not os.path.isfile(fileurl):
            return None
        f = open(fileurl, 'r')
        if not f :
            #logger.info ("open file %s failed" % servicelistfile)
            return None
        return json.loads(f.read())

    def do_getconfpath(self, services, service, filepath, multinode):
        serviceconfpath = ''
        #load servicelist
        servicelist = None
        servicelist = self.load_file(filepath+'/service.list')
        if servicelist is None:
            return serviceconfpath
        #get service config path
        if multinode is True :
            if services in servicelist['multi-node'].keys() and service in servicelist['multi-node'][services].keys():
                serviceconfpath = servicelist['multi-node'][services][service]
        else :
            if service in servicelist['one-node'].keys() :
                serviceconfpath = servicelist['one-node'][service]
        return serviceconfpath

    def get_serviceconf(self, services, service, publicpath, privatepath, multinode):
        serviceconf = None
        serviceconfpath = ''
        serviceconfpath = self.do_getconfpath(services, service, privatepath, multinode)
        if serviceconfpath is '' :
            serviceconfpath = self.do_getconfpath(services, service, publicpath, multinode)
        if serviceconfpath is '' :
            return serviceconf
        serviceconf = self.load_file(privatepath+serviceconfpath)
        if serviceconf is None:
            serviceconf = self.load_file(publicpath+serviceconfpath)
        return serviceconf

    def parse_multinodes(self, multinodes, publicpath, imagename, imageowner, imagetype):
        privatepath = self.FS_PREFIX+'/global/images/'+imagetype+'/'+imageowner+'/'+imagename+'/home/init.c'
        if imagename is 'base':
            privatepath = publicpath
        servicelist = multinodes.split('+')
        mservice = []
        oservice = []
        for service in servicelist:
            serviceconf = self.get_serviceconf(multinodes, service, publicpath, privatepath, True)
            if serviceconf is None:
                continue
            else :
                if 'one' in serviceconf.keys():
                    oservice.append(service)
                else :
                    mservice.append(service)
        return [oservice, mservice]

    def do_gencmd(self, info, i, publicpath, privatepath):
        servicecmd = []
        clusterservices = info['services']['clusterservices']
        services = info['services']['host-'+str(i)]
        for service in services.keys():
            serviceconf = self.get_serviceconf(clusterservices, service, publicpath, privatepath, services[service] is 'multi-node')
            if 'one' in serviceconf.keys():
                script = serviceconf['one']['path'] + ' ' + serviceconf['one']['params']
                servicecmd.append(script)
            else :
                if i == 0:
                    script = serviceconf['master']['path'] + ' ' + self.replace_params(serviceconf['master']['params'], info['services'])
                    servicecmd.append(script)
                script = serviceconf['slave']['path'] + ' ' + self.replace_params(serviceconf['slave']['params'], info['services'])
                servicecmd.append(script)
        return servicecmd

    def replace_params(self, script, services):
        script = script.replace("$MASTER$", services['master'])
        return script

    def get_containerindex(self, clusterinfo, containername):
        containers = clusterinfo['containers']
        index = 0
        for container in containers:
            if cmp(containername, container['containername']) == 0:
                return index
            index = index + 1
        return 0

    def exists_path(self, path, name):
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(path + '/' + name):
            result = {}
            result['multi-node'] = {}
            result['one-node'] = {}
            f = open(path+'/'+name, 'w')
            f.write(json.dumps(result))
            f.close()
        return True

    def __init__(self):
        #self.FS_PREFIX = env.getenv('FS_PREFIX')
        self.FS_PREFIX = "/opt/docklet"

    def list_service(self, imagename, imageowner, imagetype):
        onenode_service = []
        multinode_service = []

        logger.info ("in list service : %s, %s, %s" % (imagename, imageowner, imagetype))

        #get system service
        servicelistpath = self.FS_PREFIX + '/local/basefs/home/init.s/service.list'
        allservice = self.load_file(servicelistpath)
        onenode_service.extend(allservice['one-node'].keys())
        multinode_service.extend(allservice['multi-node'].keys())

        #get image service
        if not imagename is 'base' :
            servicelistpath = self.FS_PREFIX + '/global/images/' + imagetype + '/' + imageowner + '/' + imagename + '/home/init.c/service.list'
            imageservice = self.load_file(servicelistpath)
            logger.info ("in list service : %s" % imageservice)
            if not imageservice is None:
                onenode_service.extend(imageservice['one-node'].keys())
                multinode_service.extend(imageservice['multi-node'].keys())

        onenode_service.sort()
        multinode_service.sort()

        result = {}
        result['onenode'] = onenode_service
        result['multinode'] = multinode_service

        return result

    def list_service2(self, username, clustername, imagename, imageowner, imagetype):
        allservices = self.list_service(imagename, imageowner, imagetype)['onenode']
        extensiveservice = []
        #get current cluster service
        clusterconfpath = self.FS_PREFIX+'/global/users/'+username+'/clusters/'+clustername
        clusterconf = self.load_file(clusterconfpath)
        clusterservices = clusterconf['services']['clusterservices']

        publicpath = self.FS_PREFIX+'/local/basefs/home/init.s'
        #if base image is chosen
        if imagename is 'base':
            privatepath = publicpath
        #if a user image is chosen
        else :
            privatepath = self.FS_PREFIX+'/global/images/'+imagetype+'/'+imageowner+'/'+imagename+'/home/init.c'

        for service in allservices:
            if service in clusterservices :
                serviceconf = self.get_serviceconf('', service, publicpath, privatepath, False)
                if serviceconf['scalable'] == 'true':
                    extensiveservice.append(service)
                    allservices.remove(service)
            else :
                continue

        allservices.sort()
        extensiveservice.sort()

        result = {}
        result['onenode'] = allservices
        result['extensive'] = extensiveservice
        return result

    def list_service3(self, username, clustername, containername):
        servicehad = []
        serviceadd = []
        clusterinfopath = self.FS_PREFIX + '/global/users/' + username + '/clusters/' + clustername
        clusterinfo = self.load_file(clusterinfopath)
        containerindex = containername.split('-')[2]
        for service in clusterinfo['services']['host-'+str(containerindex)].keys():
            servicehad.append(service)

        publicpath = self.FS_PREFIX + '/local/basefs/home/init.s'
        if os.path.exists(publicpath):
            servicelist = self.load_file(publicpath + '/service.list')
            if not servicelist is None:
                serviceadd.extend(servicelist['one-node'].keys())
        privatepath = self.FS_PREFIX + '/local/volume/' + containername + '/upper/home/init.c'
        if os.path.exists(privatepath):
            servicelist = self.load_file(privatepath + '/service.list')
            if not servicelist is None:
                serviceadd.extend(servicelist['one-node'].keys())

        for service in servicehad :
            if service in serviceadd:
                serviceadd.remove(service)

        serviceadd.sort()
        servicehad.sort()

        result = {}
        result['servicehad'] = servicehad
        result['serviceadd'] = serviceadd
        return result

    def list_service4(self, imagename, imageowner, imagetype):
        allservices = self.list_service(imagename, imageowner, imagetype)
        logger.info ("in list service4 : %s" % allservices)
        for item in allservices['multinode']:
            if not '+' in item:
                allservices['multinode'].remove(item)
        return allservices


    def create_service(self, username, clustername, image, onenode, multinodes):
        logger.info ('in create service : %s, %s' % (onenode, multinodes))
        imagename = image['name']
        imageowner = image['owner']
        imagetype = image['type']
        #servicepath = self.FS_PREFIX+'/global/users/'+username+'/clusters/'+clustername+'.service'
        publicpath = self.FS_PREFIX+'/local/basefs/home/init.s'
        #services initialization
        clustersize = 1
        services = {}
        services['host-0'] = {}
        services['clusterservices'] = []
        services['master'] = 'host-0'
        #one node cluster or multinode cluster
        if onenode is None and multinodes is None:
            return [clustersize, services]
        elif multinodes is None:
            if isinstance(onenode, str):
                services['host-0'][onenode] = "one-node"
                services['clusterservices'].append(onenode)
            else:
                for service in onenode:
                    services['host-0'][service] = "one-node"
                    services['clusterservices'].append(service)
        else :
            clustersize = 2
            services['clusterservices'].append(multinodes)
            [oservice, mservice] = self.parse_multinodes(multinodes, publicpath, imagename, imageowner, imagetype)
            logger.info ("in create service : %s, %s" % (oservice, mservice))
            olen = len(oservice)
            mlen = len(mservice)
            if olen > clustersize:
                clustersize = olen
            for i in range(0, clustersize):
                services['host-'+str(i)] = {}
                if olen > i:
                    services['host-'+str(i)][oservice[i]] = "multi-node"
                for j in range(0, mlen):
                    services['host-'+str(i)][mservice[j]] = "multi-node"

        #logger.info ('service file content : %s' % services)
        #servicefile = open(servicepath, 'w')
        #servicefile.write(json.dumps(services))
        #servicefile.close()
        return [clustersize, services]

    def scale_out(self, username, clustername, info, cid, extensive, onenode, image):
        services = info['services']
        newhost = {}
        if extensive is None and onenode is None:
            return [services, []]
        #deal with onenode services
        if not onenode is None :
            if isinstance(onenode, str):
                if not onenode in services['clusterservices'] :
                    services['clusterservices'].append(onenode)
                newhost[onenode] = 'one-node'
            else :
                for one in onenode:
                    if not one in services['clusterservices'] :
                        services['clusterservices'].append(one)
                    newhost[one] = 'one-node'
        #deal with extensive services
        if not extensive is None :
            if isinstance(extensive, str):
                for i in range(0, cid):
                    services["host-"+str(i)][extensive] = 'multi-node'
                newhost[extensive] = 'multi-node'
            else :
                for ex in extensive:
                    for i in range(0, cid):
                        services["host-"+str(i)][ex] = 'multi-node'
                    newhost[ex] = 'multi-node'
        services['host-'+str(cid)] = newhost

        imagename = image['name']
        imageowner = image['owner']
        imagetype = image['type']
        publicpath = self.FS_PREFIX+'/local/basefs/home/init.s'
        privatepath = ''
        #if base image is chosen
        if imagename is 'base':
            privatepath = publicpath
        #if a user image is chosen
        else :
            privatepath = self.FS_PREFIX+'/global/images/'+imagetype+'/'+imageowner+'/'+imagename+'/home/init.c'
        cmd = self.do_gencmd(info, cid, publicpath, privatepath)
        logger.info ('services is %s, command is %s' % (services, cmd))
        return [services, cmd]

    def gen_servicecmd(self, clustername, username, info):
        publicpath = self.FS_PREFIX+'/local/basefs/home/init.s'
        clustersize = info['size']
        servicecmdlist = []
        for i in range(0, clustersize):
            containername = info['containers'][i]['containername']
            privatepath = self.FS_PREFIX+'/local/volume/'+containername+"/upper/home/init.c"
            servicecmd = self.do_gencmd(info, i, publicpath, privatepath)
            servicecmdlist.append(servicecmd)
        return servicecmdlist

    def config_service(self, username, clustername, containername, servicelist):
        result = {}
        result['success'] = 'SUCCESS'
        if servicelist is None or servicelist == '':
            return result
        clusterinfopath = self.FS_PREFIX + '/global/users/' + username + '/clusters/' + clustername
        clusterinfo = self.load_file(clusterinfopath)
        containerindex = containername.split('-')[2]
        allservices = clusterinfo['services']
        hostservice = allservices['host-' + str(containerindex)]
        services = servicelist.split(';')
        for service in services:
            if not service in clusterinfo['services']['clusterservices']:
                clusterinfo['services']['clusterservices'].append(service)
            if not service in clusterinfo['services']['host-' + str(containerindex)].keys():
                clusterinfo['services']['host-' + str(containerindex)][service] = 'one-node'

        clusterfile = open(clusterinfopath, 'w')
        clusterfile.write(json.dumps(clusterinfo))
        clusterfile.close()

        return result

    def combine_service(self, imagename, imageowner, imagetype, servicename):
        result = {}
        result['success'] = 'SUCCESS'
        if servicename is None or servicename == '':
            return result
        services = servicename.split('+')
        rootpath = self.FS_PREFIX + '/local/basefs/home/init.s'
        upperpath = self.FS_PREFIX + '/global/images/' + imagetype + '/' + imageowner + '/' + imagename + '/home/init.c'
        self.exists_path(upperpath, 'service.list')
        rootfile = self.load_file(rootpath+'/service.list')
        upperfile = self.load_file(upperpath+'/service.list')
        combineservice = {}
        for service in services:
            if service in upperfile['one-node'].keys():
                combineservice[service] = upperfile['one-node'][service]
            elif service in rootfile['one-node'].keys():
                combineservice[service] = rootfile['one-node'][service]
        upperfile['multi-node'][servicename] = combineservice
        f = open(upperpath+'/service.list', 'w')
        f.write(json.dumps(upperfile))
        f.close()
        return result

if __name__ == '__main__':
    smgr = ServiceMgr()
    infopath = "/opt/docklet/global/users/root/clusters/test"
    info = smgr.load_file(infopath)
    print ("info is : %s" % info)
    cmd = smgr.gen_servicecmd('test', 'root', info)
