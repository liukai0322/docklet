#!/usr/bin/python

import subprocess,re,sys,etcdlib
import time,threading,json,traceback

from log import logger

class Container_Collector(threading.Thread):
    
    def __init__(self,etcdaddr,cluster_name,host,cpu_quota,mem_quota):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.host = host
        self.etcdser = etcdlib.Client(etcdaddr,"/%s/monitor" % (cluster_name))
        self.etcdser.setkey('/cpu_quota', cpu_quota)
        self.etcdser.setkey('/mem_quota', mem_quota)
        self.cpu_quota = float(cpu_quota)/100000.0
        self.mem_quota = float(mem_quota)*1000000/1024
        self.interval = 2
        return 
    
    def list_container(self):
        output = subprocess.check_output(["sudo lxc-ls"],shell=True)
        output = output.decode('utf-8')
        containers = re.split('\s+',output)
        return containers
    
    def collect_containerinfo(self,container_name):
        output = subprocess.check_output("sudo lxc-info -n %s" % (container_name),shell=True)
        output = output.decode('utf-8')
        parts = re.split('\n',output)
        info = {}
        basic_info = {}
        for part in parts:
            if not part == '':
                key_val = re.split(':',part)
                key = key_val[0]
                val = key_val[1]
                info[key] = val.lstrip()
        basic_info['Name'] = info['Name']
        basic_info['State'] = info['State']
        if(info['State'] == 'STOPPED'):
            self.etcdser.setkey('/%s/basic_info'%(container_name), basic_info)
            return False
        basic_info['PID'] = info['PID']
        basic_info['IP'] = info['IP']
        self.etcdser.setkey('/%s/basic_info'%(container_name), basic_info)
        cpu_parts = re.split(' +',info['CPU use'])
        cpu_val = cpu_parts[0].strip()
        cpu_unit = cpu_parts[1].strip()
        res = self.etcdser.getkey('/%s/cpu_use/val'%(container_name))
        cpu_last = 0
        if res[0] == True:
            cpu_last = float(res[1])
        self.etcdser.setkey('/%s/cpu_use/val'%(container_name), cpu_val)
        self.etcdser.setkey('/%s/cpu_use/unit'%(container_name), cpu_unit)
        cpu_usedp = (float(cpu_val)-float(cpu_last))/(self.cpu_quota*self.interval*1.3)
        if(cpu_usedp > 1):
            cpu_usedp = 1
        self.etcdser.setkey('/%s/cpu_use/usedp'%(container_name), cpu_usedp)
        mem_parts = re.split(' +',info['Memory use'])
        mem_val = mem_parts[0].strip()
        mem_unit = mem_parts[1].strip()
        self.etcdser.setkey('/%s/mem_use/val'%(container_name), mem_val)
        self.etcdser.setkey('/%s/mem_use/unit'%(container_name), mem_unit)
        if(mem_unit == "MiB"):
            mem_val = float(mem_val) * 1024
        mem_usedp = float(mem_val) / self.mem_quota
        self.etcdser.setkey('/%s/mem_use/usedp'%(container_name), mem_usedp)
        #print(output)
        #print(parts)
        return True
    
    def run(self):
        cnt = 0
        while not self.thread_stop:
            containers = self.list_container()
            countR = 0
            conlist = []
            for container in containers:
                if not container == '':
                    conlist.append(container)
                    try:
                        if(self.collect_containerinfo(container)):
                            countR += 1
                    except Exception as err:
                        #pass
                        logger.warning(err)
            containers_num = len(containers)-1
            self.etcdser.setkey('/%s/containers/total'%(self.host), containers_num)
            self.etcdser.setkey('/%s/containers/running'%(self.host), countR)
            time.sleep(self.interval)
            if cnt == 0:
                self.etcdser.setkey('/%s/containerslist'%(self.host), conlist)
            cnt = (cnt+1)%5
        return
    
    def stop(self):
        self.thread_stop = True


class Collector(threading.Thread):
    
    def __init__(self,etcdaddr,cluster_name,host):
        threading.Thread.__init__(self)
        self.host = host
        self.thread_stop = False
        self.etcdser = etcdlib.Client(etcdaddr,"/%s/monitor/%s" % (cluster_name,host))
        self.interval = 1
        return

    def collect_meminfo(self):
        output = subprocess.check_output(["free"],shell=True)
        output = output.decode('utf-8')
        parts = re.split('\n',output)
        memparts = re.split(' +',parts[1])
        self.etcdser.setkey('/meminfo/total',memparts[1])
        self.etcdser.setkey('/meminfo/used',memparts[2])
        self.etcdser.setkey('/meminfo/free',memparts[3])
        self.etcdser.setkey('/meminfo/shared',memparts[4])
        self.etcdser.setkey('/meminfo/buffers',memparts[5])
        self.etcdser.setkey('/meminfo/cached',memparts[6])
        #print(output)  
        #print(memparts)
        return
    
    def collect_cpuinfo(self):
        output = subprocess.check_output(["vmstat 1 2"],shell=True)
        output = output.decode('utf-8')
        parts = output.split('\n')
        cpuparts = re.split(' +',parts[3])
        self.etcdser.setkey('/cpuinfo/us', cpuparts[13])
        self.etcdser.setkey('/cpuinfo/sy', cpuparts[14])
        self.etcdser.setkey('/cpuinfo/id', cpuparts[15])
        self.etcdser.setkey('/cpuinfo/wa', cpuparts[16])
        output = subprocess.check_output(["cat /proc/cpuinfo"],shell=True)
        output = output.decode('utf-8')
        parts = output.split('\n')
        info = []
        idx = -1
        for part in parts:
            if not part == '':
                key_val = re.split(':',part)
                key = key_val[0].rstrip()
                if key == 'processor':
                    info.append({})
                    idx += 1
                val = key_val[1].lstrip()
                if key=='processor' or key=='model name' or key=='core id' or key=='cpu MHz' or key=='cache size' or key=='physical id':
                    info[idx][key] = val
        self.etcdser.setkey('/cpuinfo/config',info)
        return

    def collect_diskinfo(self):
        output = subprocess.check_output(["df","-h"],shell=True)
        output = output.decode('utf-8')
        parts = re.split('\n',output)
        setval = []
        for part in parts:
            if part.startswith("/dev/s") or part.startswith("/dev/h"):
                diskparts = re.split(' +',part)
                diskval = {}
                diskval['filesystem'] = diskparts[0]
                diskval['total'] = diskparts[1]
                diskval['used'] = diskparts[2]
                diskval['free'] = diskparts[3]
                diskval['usedp'] = diskparts[4].rstrip("%")
                setval.append(diskval)
        self.etcdser.setkey('/diskinfo', setval)
        #self.etcdser.setkey('/diskinfo/filesystem', diskparts[0])
        #self.etcdser.setkey('/diskinfo/total', diskparts[1])
        #self.etcdser.setkey('/diskinfo/used', diskparts[2])
        #self.etcdser.setkey('/diskinfo/free', diskparts[3])
        #self.etcdser.setkey('/diskinfo/usedp', diskparts[4].rstrip("%"))
        #print(output)
        #print(diskparts)
        return

    def collect_osinfo(self):
        res = {}
        output = subprocess.check_output(["cat /etc/issue.net"],shell=True)
        output = output.decode('utf-8')
        res["OSIssue"] = output.rstrip('\n')
        output = subprocess.check_output(["uname -s"],shell=True)
        output = output.decode('utf-8')
        res["OSKname"] = output.rstrip('\n')
        output = subprocess.check_output(["uname -r"],shell=True)
        output = output.decode('utf-8')
        res["OSKrelease"] = output.rstrip('\n')
        output = subprocess.check_output(["uname -v"],shell=True)
        output = output.decode('utf-8')
        res["OSKversion"] = output.rstrip('\n')
        output = subprocess.check_output(["uname -m"],shell=True)
        output = output.decode('utf-8')
        res["OSKmachine"] = output.rstrip('\n')
        self.etcdser.setkey('/osinfo',res)
        return
    
    def run(self):
        self.collect_osinfo()
        while not self.thread_stop:
            self.collect_meminfo()
            self.collect_cpuinfo()
            self.collect_diskinfo()
            self.etcdser.setkey('/running','True',6)
            time.sleep(self.interval)
            #   print(self.etcdser.getkey('/meminfo/total'))
        return
    
    def stop(self):
        self.thread_stop = True

class Container_Fetcher:
    def __init__(self,etcdaddr,cluster_name):
        self.etcdser = etcdlib.Client(etcdaddr,"/%s/monitor" % (cluster_name))
        return

    def get_cpu_use(self,container_name):
        res = {}
        res['quota'] = self.etcdser.getkey('/cpu_quota')[1]
        res['val'] = self.etcdser.getkey('/%s/cpu_use/val'%(container_name))[1]
        res['unit'] = self.etcdser.getkey('/%s/cpu_use/unit'%(container_name))[1]
        res['usedp'] = self.etcdser.getkey('/%s/cpu_use/usedp'%(container_name))[1]
        return res

    def get_mem_use(self,container_name):
        res = {}
        res['quota'] = self.etcdser.getkey('/mem_quota')[1]
        res['val'] = self.etcdser.getkey('/%s/mem_use/val'%(container_name))[1]
        res['unit'] = self.etcdser.getkey('/%s/mem_use/unit'%(container_name))[1]
        res['usedp'] = self.etcdser.getkey('/%s/mem_use/usedp'%(container_name))[1]
        return res
    
    def get_basic_info(self,container_name):
        res = self.etcdser.getkey("/%s/basic_info"%(container_name))
        if res[0] == False:
            return {}
        res = dict(eval(res[1]))
        return res

class Fetcher:

    def __init__(self,etcdaddr,cluster_name,host):
        self.etcdser = etcdlib.Client(etcdaddr,"/%s/monitor/%s" % (cluster_name,host))
        return  

    #def get_clcnt(self):
    #   return DockletMonitor.clcnt
    
    #def get_nodecnt(self):
    #   return DockletMonitor.nodecnt

    #def get_meminfo(self):
    #   return self.get_meminfo_('172.31.0.1')

    def get_meminfo(self):
        res = {}
        res['total'] = self.etcdser.getkey('/meminfo/total')[1]
        res['used'] = self.etcdser.getkey('/meminfo/used')[1]
        res['free'] = self.etcdser.getkey('/meminfo/free')[1]
        res['shared'] = self.etcdser.getkey('/meminfo/shared')[1]
        res['buffers'] = self.etcdser.getkey('/meminfo/buffers')[1]
        res['cached'] = self.etcdser.getkey('/meminfo/cached')[1]
        return res

    def get_cpuinfo(self):
        res = {}
        res['us'] = self.etcdser.getkey('/cpuinfo/us')[1]
        res['sy'] = self.etcdser.getkey('/cpuinfo/sy')[1]
        res['id'] = self.etcdser.getkey('/cpuinfo/id')[1]
        res['wa'] = self.etcdser.getkey('/cpuinfo/wa')[1]
        #res['st'] = self.etcdser.getkey('/cpuinfo/st')[1]
        return res

    def get_cpuconfig(self):
        res = {}
        [ret, ans] = self.etcdser.getkey('/cpuinfo/config')
        if ret == True :
            res = list(eval(ans))
            return res
        else:
            logger.warning(ans)
            return res

    def get_diskinfo(self):
        res = []
        [ret, ans] = self.etcdser.getkey('/diskinfo')
        if ret == True :
            res = list(eval(ans))
            return res
        else:
            logger.warning(ans)
            return res

    def get_osinfo(self):
        res = {}
        [ret, ans] = self.etcdser.getkey('/osinfo')
        if ret == True:
            res = dict(eval(ans))
            return res
        else:
            logger.warning(ans)
            return res

    def get_containers(self):
        res = {}
        res['total'] = self.etcdser.getkey('/containers/total')[1]
        res['running'] = self.etcdser.getkey('/containers/running')[1]
        return res

    def get_status(self):
        isexist = self.etcdser.getkey('/running')[0]
        if(isexist):
            return 'RUNNING'
        else:
            return 'STOPPED'

    def get_containerslist(self):
        res = list(eval(self.etcdser.getkey('/containerslist')[1]))
        return res
