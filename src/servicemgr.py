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
            logger.info ("open file %s failed" % servicelistfile)
            return None
        return json.loads(f.read())

    def do_getconf(self, services, service, filepath, multinode):
        servicelist = None
        serviceconf = None
        #load servicelist
        servicelist = self.load_file(filepath+'/service.list')
        if servicelist is None:
            return serviceconf
        #get service config path
        serviceconfpath = ''
        if multinode is True :
            if services in servicelist['multi-node'].keys() and service in servicelist['multi-node'][services].keys():
                serviceconfpath = servicelist['multi-node'][services][service]
        else :
            if service in servicelist['one-node'].keys() :
                serviceconfpath = servicelist['one-node'][service]
        if serviceconfpath is '':
            return serviceconf

        serviceconf = self.load_file(filepath+serviceconfpath)
        return serviceconf

    def get_serviceconf(self, services, service, publicpath, privatepath, multinode):
        serviceconf = None
        serviceconf = self.do_getconf(services, service, privatepath, multinode)
        if serviceconf is None :
            serviceconf = self.do_getconf(services, service, publicpath, multinode)
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

    def __init__(self):
        #self.FS_PREFIX = env.getenv('FS_PREFIX')
        self.FS_PREFIX = "/opt/docklet"

    def list_service(self, imagename, imageowner, imagetype):
        onenode_service = []
        multinode_service = []

        #get system service
        servicelistpath = self.FS_PREFIX + '/local/basefs/home/init.s/service.list'
        allservice = self.load_file(servicelistpath)
        onenode_service.extend(allservice['one-node'].keys())
        multinode_service.extend(allservice['multi-node'].keys())

        #get image service
        if not imagename is 'base' :
            servicelistpath = self.FS_PREFIX + '/global/images/' + imagetype + '/' + imageowner + '/' + imagename + '/home/init.c/service.list'
            imageservice = self.load_file(servicelistpath)
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

    def create_service(self, username, clustername, image, onenode, multinodes):
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

        logger.info ('service file content : %s' % services)
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


if __name__ == '__main__':
    smgr = ServiceMgr()
    infopath = "/opt/docklet/global/users/root/clusters/test"
    info = smgr.load_file(infopath)
    print ("info is : %s" % info)
    cmd = smgr.gen_servicecmd('test', 'root', info)
