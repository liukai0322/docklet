#!/usr/bin/python3

import json, sys, netifaces, subprocess

from log import logger
import env

# getip : get ip from network interface
# ifname : name of network interface
def getip(ifname):
    if ifname not in netifaces.interfaces():
        return False # No such interface
    else:
        addrinfo = netifaces.ifaddresses(ifname)
        if 2 in addrinfo:
            return netifaces.ifaddresses(ifname)[2][0]['addr']
        else:
            return False # network interface is down

# netsetup : setup network, use netsetup.sh to do this work
#       1. initialize bridges
#       2. setup GRE tunnels
def netsetup(action, ip):
    path = env.getenv("DOCKLET_LIB")
    if action == 'init':
        logger.info ("initialize bridges")
    else:
        logger.info ("setup GRE tunnel")
    # subprocess.getstatusoutput will get status and output
    #                      and arg must be a string
    #[status, output] = subprocess.getstatusoutput(path+"/netsetup.sh "+action+" "+ip)
    # subprocess.call will print the result to console
    #                      and args must be a list of string
    logger.debug ("calling netsetup.sh %s %s" % (action, ip))
    subprocess.call([path+"/netsetup.sh", action, ip])

def init_gateway(gwname, gwip, vlanid):
    path = env.getenv("DOCKLET_LIB")
    logger.info("init gateway for %s with %s tag=%s" % (gwname, gwip, str(vlanid)) )
    subprocess.call([path+"/netsetup.sh", "newgw", gwname, gwip, str(vlanid)])

def del_gateway(gwname):
    path = env.getenv("DOCKLET_LIB")
    logger.info("delete gateway for %s" % gwname )
    subprocess.call([path+"/netsetup.sh", "delgw", gwname])

def ip_to_int(addr):
    [a, b, c, d] = addr.split('.')
    return (int(a)<<24) + (int(b)<<16) + (int(c)<<8) + int(d)

def int_to_ip(num):
    return str((num>>24)&255)+"."+str((num>>16)&255)+"."+str((num>>8)&255)+"."+str(num&255)

# fix addr with cidr, for example, 172.16.0.10/24 --> 172.16.0.0/24
def fix_ip(addr, cidr):
    return int_to_ip( ip_to_int(addr) & ( (-1) << (32-int(cidr)) ) )
    #return int_to_ip(ip_to_int(addr) & ( ~( (1<<(32-int(cidr)))-1 ) ) )

# jump to next interval address with cidr
def next_interval(addr, cidr):
    addr = fix_ip(addr, int(cidr))
    return int_to_ip(ip_to_int(addr)+(1<<(32-int(cidr))))

# jump to before interval address with cidr
def before_interval(addr, cidr):
    addr = fix_ip(addr, int(cidr))
    addrint = ip_to_int(addr)-(1<<(32-int(cidr)))
    # addrint maybe negative
    if addrint < 0:
        return "-1.-1.-1.-1"
    else:
        return int_to_ip(addrint)


# IntervalPool :  manage network blocks with IP/CIDR
# Data Structure :
#       ... ...
#       cidr=16 : A1, A2, ...      # A1 is an IP, means an interval [A1, A1+2^16-1], equals to A1/16
#       cidr=17 : B1, B2, ...
#       ... ...
# API :
#       allocate
#       free
class IntervalPool(object):
    # cidr : 1,2, ..., 32
    def __init__(self, addr_cidr=None, copy=None):
        if addr_cidr:
            self.pool = {}
            [addr, cidr] = addr_cidr.split('/')
            cidr = int(cidr)
            # fix addr with cidr, for example, 172.16.0.10/24 --> 172.16.0.0/24
            addr = fix_ip(addr, cidr)
            self.info = addr+"/"+str(cidr)
            # init interval pool
            #   cidr   : [ addr ]
            #   cidr+1 : [ ]
            #   ...
            #   32     : [ ]
            self.pool[str(cidr)]=[addr]
            for i in range(cidr+1, 33):
                self.pool[str(i)]=[]
        elif copy:
            self.info = copy['info']
            self.pool = copy['pool']
        else:
            logger.error("IntervalPool init failed with no addr_cidr or center")

    def __str__(self):
        return json.dumps({'info':self.info, 'pool':self.pool})

    def printpool(self):
        cidrs = list(self.pool.keys())
        # sort with key=int(cidr)
        cidrs.sort(key=int)
        for i in cidrs:
            print (i + " : " + str(self.pool[i]))

    # allocate an interval with CIDR
    def allocate(self, thiscidr):
        # thiscidr -- cidr for this request
        # upcidr -- up stream which has interval to allocate
        thiscidr=int(thiscidr)
        upcidr = thiscidr
        # find first cidr who can allocate enough ips
        while((str(upcidr) in self.pool) and  len(self.pool[str(upcidr)])==0):
            upcidr = upcidr-1
        if str(upcidr) not in self.pool:
            return [False, 'Not Enough to Allocate']
        # get the block/interval to allocate ips
        upinterval = self.pool[str(upcidr)][0]
        self.pool[str(upcidr)].remove(upinterval)
        # split the upinterval and put the rest intervals back to interval pool
        for i in range(int(thiscidr), int(upcidr), -1):
            self.pool[str(i)].append(next_interval(upinterval, i))
            #self.pool[str(i)].sort(key=ip_to_int)  # cidr between thiscidr and upcidr are null, no need to sort
        return [True, upinterval]

    # deallocate an interval with IP/CIDR
    # ToDo : when free IP/CIDR, we donot check whether IP/CIDR is in pool
    #        maybe we check this later
    def free(self, addr, cidr):
        cidr = int(cidr)
        # cidr not in pool means CIDR out of pool range
        if str(cidr) not in self.pool:
            return [False, 'CIDR not in pool']
        addr = fix_ip(addr, cidr)
        # merge interval and move to up cidr
        while(True):
            # cidr-1 not in pool means current CIDR is the top CIDR
            if str(cidr-1) not in self.pool:
                break
            # if addr can satisfy cidr-1, and next_interval also exist,
            #           merge addr with next_interval to up cidr (cidr-1)
            # if addr not satisfy cidr-1, and before_interval exist,
            #           merge addr with before_interval to up cidr, and interval index is before_interval
            if addr == fix_ip(addr, cidr-1):
                if next_interval(addr, cidr) in self.pool[str(cidr)]:
                    self.pool[str(cidr)].remove(next_interval(addr,cidr))
                    cidr=cidr-1
                else:
                    break
            else:
                if before_interval(addr, cidr) in self.pool[str(cidr)]:
                    addr = before_interval(addr, cidr)
                    self.pool[str(cidr)].remove(addr)
                    cidr = cidr - 1
                else:
                    break
        self.pool[str(cidr)].append(addr)
        # sort interval with key=ip_to_int(IP)
        self.pool[str(cidr)].sort(key=ip_to_int)
        return [True, "Free success"]

# EnumPool : manage network ips with ip or ip list
# Data Structure : [ A, B, C, ... X ] , A is a IP address
class EnumPool(object):
    def __init__(self, addr_cidr=None, copy=None):
        if addr_cidr:
            self.pool = []
            [addr, cidr] = addr_cidr.split('/')
            cidr=int(cidr)
            addr=fix_ip(addr, cidr)
            self.info = addr+"/"+str(cidr)
            # init enum pool
            # first IP is network id, last IP is network broadcast address
            # first and last IP can not be allocated
            for i in range(1, pow(2, 32-cidr)-1):
                self.pool.append(int_to_ip(ip_to_int(addr)+i))
        elif copy:
            self.info = copy['info']
            self.pool = copy['pool']
        else:
            logger.error("EnumPool init failed with no addr_cidr or copy")

    def __str__(self):
        return json.dumps({'info':self.info, 'pool':self.pool})

    def printpool(self):
        print (str(self.pool))

    def acquire(self, num=1):
        if num > len(self.pool):
            return [False, "No enough IPs"]
        result = []
        for i in range(0, num):
            result.append(self.pool.pop())
        return [True, result]

    def acquire_cidr(self, num=1):
        [status, result] = self.acquire(num)
        if not status:
            return [status, result]
        return [True, list(map(lambda x:x+"/"+self.info.split('/')[1], result))]

    # ToDo : when release :
    #               not check whether IP is in the range of pool
    #               not check whether IP is already in the pool
    def release(self, ip_or_ips):
        if type(ip_or_ips) == str:
            ips = [ ip_or_ips ]
        else:
            ips = ip_or_ips
        for ip in ips:
            # maybe ip is in format IP/CIDR
            ip = ip.split('/')[0]
            self.pool.append(ip)
        return [True, "release success"]

# wrap EnumPool with vlanid and gateway
class UserPool(EnumPool):
    def __init__(self, addr_cidr=None, vlanid=None, copy=None):
        if addr_cidr and vlanid:
            EnumPool.__init__(self, addr_cidr = addr_cidr)
            self.vlanid=vlanid
            self.pool.sort(key=ip_to_int)
            self.gateway = self.pool[0]
            self.pool.remove(self.gateway)
        elif copy:
            EnumPool.__init__(self, copy = copy)
            self.vlanid = int(copy['vlanid'])
            self.gateway = copy['gateway']
        else:
            logger.error("UserPool init failed with no addr_cidr or copy")

    def get_gateway(self):
        return self.gateway

    def get_gateway_cidr(self):
        return self.gateway+"/"+self.info.split('/')[1]

    def printpool(self):
        print("users ID:"+str(self.vlanid)+",  net info:"+self.info+",  gateway:"+self.gateway)
        print (str(self.pool))

# NetworkMgr : mange docklet network ip address
#   center : interval pool to allocate and free network block with IP/CIDR
#   system : enumeration pool to acquire and release system ip address
#   users : set of users' enumeration pools to manage users' ip address
class NetworkMgr(object):
    def __init__(self, addr_cidr, etcdclient, mode):
        self.etcd = etcdclient
        if mode == 'new':
            logger.info("init network manager with %s" % addr_cidr)
            self.center = IntervalPool(addr_cidr=addr_cidr)
            # allocate a pool for system IPs, use CIDR=27, has 32 IPs
            syscidr = 27
            [status, sysaddr] = self.center.allocate(syscidr)
            if status == False:
                logger.error ("allocate system ips in __init__ failed")
                sys.exit(1)
            # maybe for system, the last IP address of CIDR is available
            # But, EnumPool drop the last IP address in its pool -- it is not important
            self.system = EnumPool(sysaddr+"/"+str(syscidr))
            self.users = {}
            self.vlanids = {}
            self.init_vlanids(4095, 60)
            self.dump_center()
            self.dump_system()
        elif mode == 'recovery':
            logger.info("init network manager from etcd")
            self.center = None
            self.system = None
            self.users = {}
            self.vlanids = {}
            self.load_center()
            self.load_system()
            self.load_vlanids()
        else:
            logger.error("mode: %s not supported" % mode)

    def init_vlanids(self, total, block):
        self.vlanids['block'] = block
        self.etcd.setkey("network/vlanids/info", str(total)+"/"+str(block))
        for i in range(1, int((total-1)/block)):
            self.etcd.setkey("network/vlanids/"+str(i), json.dumps(list(range(1+block*(i-1), block*i+1))))
        self.vlanids['currentpool'] = list(range(1+block*i, total+1))
        self.vlanids['currentindex'] = i+1
        self.etcd.setkey("network/vlanids/"+str(i+1), json.dumps(self.vlanids['currentpool']))
        self.etcd.setkey("network/vlanids/current", str(i+1))

    def load_vlanids(self):
        [status, info] = self.etcd.getkey("network/vlanids/info")
        self.vlanids['block'] = int(info.split("/")[1])
        [status, current] = self.etcd.getkey("network/vlanids/current")
        self.vlanids['currentindex'] = int(current)
        if self.vlanids['currentindex'] == 0:
            self.vlanids['currentpool'] = []
        else:
            [status, pool]= self.etcd.getkey("network/vlanids/"+str(self.vlanids['currentindex']))
            self.vlanids['currentpool'] = json.loads(pool)

    def dump_vlanids(self):
        if self.vlanids['currentpool'] == []:
            if self.vlanids['currentindex'] != 0:
                self.etcd.delkey("network/vlanids/"+str(self.vlanids['currentindex']))
                self.etcd.setkey("network/vlanids/current", str(self.vlanids['currentindex']-1))
            else:
                pass
        else:
            self.etcd.setkey("network/vlanids/"+str(self.vlanids['currentindex']), json.dumps(self.vlanids['currentpool']))

    def load_center(self):
        [status, centerdata] = self.etcd.getkey("network/center")
        center = json.loads(centerdata)
        self.center = IntervalPool(copy = center)

    def dump_center(self):
        self.etcd.setkey("network/center", json.dumps({'info':self.center.info, 'pool':self.center.pool}))

    def load_system(self):
        [status, systemdata] = self.etcd.getkey("network/system")
        system = json.loads(systemdata)
        self.system = EnumPool(copy=system)

    def dump_system(self):
        self.etcd.setkey("network/system", json.dumps({'info':self.system.info, 'pool':self.system.pool}))

    def load_user(self, username):
        [status, userdata] = self.etcd.getkey("network/users/"+username)
        usercopy = json.loads(userdata)
        user = UserPool(copy = usercopy)
        self.users[username] = user
        
    def dump_user(self, username):
        self.etcd.setkey("network/users/"+username, json.dumps({'info':self.users[username].info, 'vlanid':self.users[username].vlanid, 'gateway':self.users[username].gateway, 'pool':self.users[username].pool}))

    def printpools(self):
        print ("<Center>")
        self.center.printpool()
        print ("<System>")
        self.system.printpool()
        print ("<users>")
        print ("    users in users is in etcd, not in memory")
        print ("<vlanids>")
        print (str(self.vlanids['currentindex'])+":"+str(self.vlanids['currentpool']))

    def acquire_vlanid(self):
        if self.vlanids['currentpool'] == []:
            if self.vlanids['currentindex'] == 0:
                return [False, "No VLAN IDs"]
            else:
                logger.error("vlanids current pool is empty with current index not zero")
                return [False, "internal error"]
        vlanid = self.vlanids['currentpool'].pop()
        self.dump_vlanids()
        if self.vlanids['currentpool'] == []:
            self.load_vlanids()
        return [True, vlanid]

    def release_vlanid(self, vlanid):
        if len(self.vlanids['currentpool']) == self.vlanids['block']:
            self.vlanids['currentpool'] = [vlanid]
            self.vlanids['currentindex'] = self.vanids['currentindex']+1
            self.dump_vlanids()
        else:
            self.vlanids['currentpool'].append(vlanid)
            self.dump_vlanids()
        return [True, "Release VLAN ID success"]

    def add_user(self, username, cidr):
        logger.info ("add user %s with cidr=%s" % (username, str(cidr)))
        if self.has_user(username):
            return [False, "user already exists in users set"]
        [status, result] = self.center.allocate(cidr) 
        if status == False:
            return [False, result]
        [status, vlanid] = self.acquire_vlanid()
        if status:
            vlanid = int(vlanid)
        else:
            self.center.free(result, cidr)
            return [False, vlanid]
        self.users[username] = UserPool(addr_cidr = result+"/"+str(cidr), vlanid=vlanid)
        init_gateway(username, self.users[username].get_gateway_cidr(), vlanid)
        self.dump_user(username)
        del self.users[username]
        return [True, 'add user success']

    def del_user(self, username):
        logger.info ("delete user %s with cidr=%s" % (username))
        if not self.has_user(username):
            return [False, username+" not in users set"]
        self.load_user(username)
        [addr, cidr] = self.users[username].info.split('/')
        self.center.free(addr, int(cidr))
        self.dump_center()
        self.release_vlanid(self.users[username].vlanid)
        del_gateway(username)
        self.etcd.deldir("network/users/"+username)
        del self.users[username]
        return [True, 'delete user success']

    def has_user(self, username):
        [status, _value] = self.etcd.getkey("network/users/"+username)
        return status

    def acquire_userips(self, username, num=1):
        logger.info ("acquire user ips of %s" % (username))
        if not self.has_user(username):
            return [False, 'username not exists in users set']
        self.load_user(username)
        result = self.users[username].acquire(num)
        self.dump_user(username)
        del self.users[username]
        return result

    def acquire_userips_cidr(self, username, num=1):
        logger.info ("acquire user ips of %s" % (username))
        if not self.has_user(username):
            return [False, 'username not exists in users set']
        self.load_user(username)
        result = self.users[username].acquire_cidr(num)
        self.dump_user(username)
        del self.users[username]
        return result

    # ip_or_ips : one IP address or a list of IPs
    def release_userips(self, username, ip_or_ips):
        logger.info ("release user ips of %s with ips: %s" % (username, str(ip_or_ips)))
        if not self.has_user(username):
            return [False, 'username not exists in users set']
        self.load_user(username)
        result = self.users[username].release(ip_or_ips)
        self.dump_user(username)
        del self.users[username]
        return result

    def get_usergw(self, username):
        if not self.has_user(username):
            return [False, 'username not exists in users set']
        self.load_user(username)
        result = self.users[username].get_gateway()
        self.dump_user(username)
        del self.users[username]
        return result

    def get_usergw_cidr(self, username):
        if not self.has_user(username):
            return [False, 'username not exists in users set']
        self.load_user(username)
        result = self.users[username].get_gateway_cidr()
        self.dump_user(username)
        del self.users[username]
        return result

    def get_uservlanid(self, username):
        if not self.has_user(username):
            return [False, 'username not exists in users set']
        self.load_user(username)
        result = self.users[username].vlanid
        self.dump_user(username)
        del self.users[username]
        return result

    def acquire_sysips(self, num=1):
        logger.info ("acquire system ips")
        result = self.system.acquire(num)
        self.dump_system()
        return result

    def acquire_sysips_cidr(self, num=1):
        logger.info ("acquire system ips")
        result = self.system.acquire_cidr(num)
        self.dump_system()
        return result

    def release_sysips(self, ip_or_ips):
        logger.info ("acquire system ips: %s" % str(ip_or_ips))
        result = self.system.release(ip_or_ips)
        self.dump_system()
        return result 


