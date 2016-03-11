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

    def loadfile(self, fileurl):
        if not os.path.isfile(fileurl):
            return None
        f = open(fileurl, 'r')
        if not f :
            logger.info ("open file %s failed" % servicelistfile)
            return None
        return json.loads(f.read())

    def get_serviceconf(self, service, publicpath, privatepath):
        serviceconf = None
        serviceconf = self.loadfile(privatepath+service+'/'+service+'.config')
        if serviceconf is None:
            serviceconf = self.loadfile(publicpath+service+'/'+service+'.config')
        return serviceconf

    def parse_multinodes(self, multinodes, publicpath, imagename, imageowner, imagetype):
        privatepath = self.FS_PREFIX+'/global/images/'+imagetype+'/'+imageowner+'/'+imagename+'/home/init.c/'
        if imagename is 'base':
            privatepath = publicpath
        servicelist = multinodes.split('+')
        mservice = []
        oservice = []
        for service in servicelist:
            serviceconf = self.get_serviceconf(service, publicpath, privatepath)
            if serviceconf is None:
                continue
            else :
                if 'one' in serviceconf.keys():
                    oservice.append(service)
                else :
                    mservice.append(service)
        return [oservice, mservice]

    def replace_params(self, script, services):
        script = script.replace("$MASTER$", services['master'])
        return script

    def __init__(self):
        #self.FS_PREFIX = env.getenv('FS_PREFIX')
        self.FS_PREFIX = "/opt/docklet"

    def list_service(self, imagename, username, isshared):
        onenode_service = []
        multinode_service = []

        #get system service
        servicelistpath = self.FS_PREFIX + '/local/basefs/home/init.s/service.list'
        allservice = self.loadfile(servicelistpath)
        onenode_service.extend(allservice['one-node'])
        multinode_service.extend(allservice['multi-node'])

        #get image service
        if not imagename is 'base' :
            servicelistpath = self.FS_PREFIX + '/global/images/' + isshared + '/' + username + '/' + imagename + '/home/init.c/service.list'
            imageservice = self.loadfile(servicelistpath)
            if not imageservice is None:
                onenode_service.extend(imageservice['one-node'])
                multinode_service.extend(imageservice['multi-node'])

        onenode_service.sort()
        multinode_service.sort()

        result = {}
        result['onenode'] = onenode_service
        result['multinode'] = multinode_service

        return result

    def create_service(self, username, clustername, image, onenode, multinodes):
        imagename = image['name']
        imageowner = image['owner']
        imagetype = image['type']
        #servicepath = self.FS_PREFIX+'/global/users/'+username+'/clusters/'+clustername+'.service'
        publicpath = self.FS_PREFIX+'/local/basefs/home/init.s/'
        clustersize = 1
        services = {}
        services['host-0'] = []
        services['master'] = 'host-0'
        #one node cluster or multinode cluster
        if onenode is None and multinodes is None:
            return [clustersize, services]
        elif multinodes is None:
            if isinstance(onenode, str):
                services['host-0'].append(onenode)
            else:
                for service in onenode:
                    services['host-0'].append(service)
        else :
            clustersize = 2
            #parse multinode services into one-node type and multi-node type
            [oservice, mservice] = self.parse_multinodes(multinodes, publicpath, imagename, imageowner, imagetype)
            olen = len(oservice)
            mlen = len(mservice)
            if olen > clustersize:
                clustersize = olen
            for i in range(0, clustersize):
                services['host-'+str(i)] = []
            for i in range(0, olen):
                services['host-'+str(i)].append(oservice[i])
            if not mservice is None:
                for i in range(0, clustersize):
                    for j in range(0, mlen):
                        services['host-'+str(i)].append(mservice[j])

        logger.info ('service file content : %s' % services)
        #servicefile = open(servicepath, 'w')
        #servicefile.write(json.dumps(services))
        #servicefile.close()
        return [clustersize, services]

    def gen_servicecmd(self, clustername, username, info):
        publicpath = self.FS_PREFIX+'/local/basefs/home/init.s/'
        clustersize = info['size']
        servicelist = []
        for i in range(0, clustersize):
            servicecmd = []
            containername = info['containers'][i]['containername']
            privatepath = self.FS_PREFIX+'/local/volume/'+containername+"/upper/home/init.c/"
            services = info['services']['host-'+str(i)]
            for service in services:
                serviceconf = self.get_serviceconf(service, publicpath, privatepath)
                if 'one' in serviceconf.keys():
                    script = serviceconf['one']['path'] + ' ' + serviceconf['one']['params']
                    servicecmd.append(script)
                else :
                    if i == 0:
                        script = serviceconf['master']['path'] + ' ' + self.replace_params(serviceconf['master']['params'], info['services'])
                        servicecmd.append(script)
                    script = serviceconf['slave']['path'] + ' ' + self.replace_params(serviceconf['slave']['params'], info['services'])
                    servicecmd.append(script)
            servicelist.append(servicecmd)
        logger.info ("services cmd is : %s" % servicelist)
        return servicelist



if __name__ == '__main__':
    smgr = ServiceMgr()
    [flag, services] = smgr.create_service('root', 'lk', 'base', 'docklet', 'base', ['ssh', 'jupyter'], None)
    print ('services returned is %s' % services)
    [flag, services] = smgr.create_service('root', 'lk', 'base', 'docklet', 'base', None, 'apache2+mysql')
    print ('services returned is %s' % services)
    [flag, services] = smgr.create_service('root', 'lk', 'base', 'docklet', 'base', None, 'spark')
    print ('services returned is %s' % services)
