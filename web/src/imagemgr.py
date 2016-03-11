#!/usr/bin/python3

"""
design:
    1. When user create an image, it will upload to an image server, at the same time, local host
    will save an image. A time file will be made with them. Everytime a container start by this
    image, the time file will update.
    2. When user save an image, if it is a update option, it will faster than create a new image.
    3. At image server and every physical host, run a shell script to delete the image, which is
    out of time.
    4. We can show every user their own images and the images are shared by other. User can new a
    cluster or scale out a new node by them. And user can remove his own images.
    5. When a remove option occur, the image server will delete it. But some physical host may 
    also maintain it. I think it doesn't matter.
    6. The manage of lvm has been including in this module.
"""


from configparser import ConfigParser
from io import StringIO
import os,sys,subprocess,time,re,datetime,threading

from log import logger
import env

class ImageMgr():
    def sys_call(self,command):
        output = subprocess.getoutput(command).strip()
        return None if output == '' else output
    
    def sys_return(self,command):
        return_value = subprocess.call(command,shell=True)
        return return_value
    
    def __init__(self):
        self.NFS_PREFIX = env.getenv('FS_PREFIX') 
        self.imgpath = self.NFS_PREFIX + "/global/images/"
        self.srcpath = env.getenv('DOCKLET_LIB') + "/" 
        self.imageserver = "192.168.6.249"
    
    def datetime_toString(self,dt):
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def string_toDatetime(self,string):
        return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
            
    def updateinfo(self,imgpath,image,description):
        image_info_file = open(imgpath+"."+image+".info",'w')
        image_info_file.writelines([self.datetime_toString(datetime.datetime.now()) + "\n", "unshare"])
        image_info_file.close()
        image_description_file = open(imgpath+"."+image+".description", 'w')
        image_description_file.write(description)
        image_description_file.close()

    def dealpath(self,fspath):
        if fspath[-1:] == "/":
            return self.dealpath(fspath[:-1])
        else:
            return fspath
    
    def createImage(self,user,image,lxc,description="Not thing",isforce = False):
        fspath = self.NFS_PREFIX + "/local/volume/" + lxc + "/upper"
        imgpath = self.imgpath + "private/" + user + "/"
        if isforce is False:
            logger.info("this save operation is not force")
            if os.path.exists(imgpath+image):
                return [False,"target image is exists"]
        self.sys_call("mkdir -p %s" % imgpath+image)
        self.sys_call("rsync -a --delete --exclude=lost+found/ --exclude=nfs/ --exclude=dev/ --exclude=mnt/ --exclude=tmp/ --exclude=media/ --exclude=proc/ --exclude=sys/ %s/ %s/" % (self.dealpath(fspath),imgpath+image))
        self.sys_call("rm -f %s" % (imgpath+"."+image+"_docklet_share"))
        self.updateinfo(imgpath,image,description)
        logger.info("image:%s from LXC:%s create success" % (image,lxc))
        return [True, "create image success"]

    def prepareImage(self,user,image,fspath):
        imagename = image['name']
        imagetype = image['type']
        imageowner = image['owner']
        if imagename == "base" and imagetype == "base":
            return
        if imagetype == "private":
            imgpath = self.imgpath + "private/" + user + "/"
        else:
            imgpath = self.imgpath + "public/" + imageowner + "/"
        self.sys_call("rsync -a --delete --exclude=lost+found/ --exclude=nfs/ --exclude=dev/ --exclude=mnt/ --exclude=tmp/ --exclude=media/ --exclude=proc/ --exclude=sys/ %s/ %s/" % (imgpath+imagename,self.dealpath(fspath)))
        #self.sys_call("rsync -a --delete --exclude=nfs/ %s/ %s/" % (imgpath+image,self.dealpath(fspath)))
        #self.updatetime(imgpath,image)
        return 
   
    def flush_one(self,user,image,lxc):
        imaget = {}
        imaget['name'] = image
        imaget['type'] = "private"
        imaget['owner'] = user
        layer = self.NFS_PREFIX + "/local/volume/" + lxc + "/upper"
        self.sys_call(self.srcpath+"lxc_control.sh stop %s" % lxc)
        logger.info("LXC:%s stop success" % lxc)
        self.prepareImage(user,imaget,layer)
        logger.info("LXC:%s rootfs prepare success" % lxc)
        self.sys_call(self.srcpath+"lxc_control.sh start %s" % lxc)
        logger.info("LXC:%s start success" % lxc)

    def flush(self,user,from_lxc,to_lxcs):
        imgpath = self.imgpath + "private" + user + "/"
        imagetmp = {}
        imagetmp['name'] = user + "_tmp_docklet"
        imagetmp['type'] = "private"
        self.createImage(user,imagetmp,from_lxc)
        logger.info("image:%s create success" % imagetmp)
        threads = []
        for to_lxc in to_lxcs:
            """
            layer = self.NFS_PREFIX + "/local/volume/" + to_lxc + "/upper"
            self.sys_call(self.srcpath+"lxc_control.sh stop %s" % to_lxc)
            logger.info("LXC:%s stop success" % to_lxc)
            self.prepareImage(user,imagetmp,layer)
            logger.info("LXC:%s rootfs prepare success" % to_lxc)
            self.sys_call(self.srcpath+"lxc_control.sh start %s" % to_lxc)
            logger.info("LXC:%s start success" % to_lxc)
            """
            t = threading.Thread(target=ImageMgr.flush_one,args=(self,user,imagetmp,to_lxc))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.removeImage(user,imagetmp)
        logger.info("image:%s remove success" % imagetmp)

        
    def newvg(self,size=1000,vgname="docklet-group",fp="/opt/docklet/local/docklet-storage"):
        logger.info("size: %s, vg: %s, fp: %s" % (size, vgname, fp))
        info=self.sys_call(self.srcpath+"lvmtool.sh new group %s %s %s" % (vgname,size,fp))
        logger.info(info)

    def recoveryvg(self,vgname="docklet-group",fp="/opt/docklet/local/docklet-storage"):
        """
        rv = self.sys_return(self.srcpath+"lvmtool.sh check group %s" % vgname)
        if rv == 1:
            self.sys_call(self.srcpath+"lvmtool.sh mount group %s %s" % (vgname,fp))
        elif rv == 2:
            self.newvg()
        else:
            pass
        """
        self.sys_call(self.srcpath+"lvmtool.sh recover group %s %s" % (vgname,fp))
    def prepareFS(self,user,image,lxc,size="200",vgname="docklet-group"):
        rootfs = "/var/lib/lxc/%s/rootfs" % lxc
        layer = self.NFS_PREFIX + "/local/volume/" + lxc + "/upper"
        #self.sys_call("mountpoint %s &>/dev/null && umount -l %s" % (rootfs,rootfs))
        #self.sys_call("mountpoint %s &>/dev/null && umount -l %s" % (layer,layer))
        #self.sys_call("rm -rf %s %s && mkdir -p %s %s" % (rootfs,layer,rootfs,layer))
        #rv = self.sys_return(self.srcpath+"lvmtool.sh check volume %s %s" % (vgname,lxc))
        #if rv == 1:
        #    self.sys_call(self.srcpath+"lvmtool.sh newvolume %s %s %s %s" % (vgname,lxc,size,layer))
        #else:
        #   self.sys_call(self.srcpath+"lvmtool.sh mount volume %s %s %s" % (vgname,lxc,layer))
        #self.sys_call("mkdir -p %s/overlay %s/work" % (layer,layer))
        #self.sys_call("mount -t overlay overlay -olowerdir=%s/local/basefs,upperdir=%s/overlay,workdir=%s/work %s" % (self.NFS_PREFIX,layer,layer,rootfs))
        self.sys_call("mount -t aufs -o br=%s=rw:%s/local/basefs=ro+wh none %s/" % (layer,self.NFS_PREFIX,rootfs))
        logger.info("FS has been prepared for user:%s lxc:%s" % (user,lxc))
        #self.prepareImage(user,image,layer+"/overlay")
        self.prepareImage(user,image,layer)
        logger.info("image has been prepared")

    def deleteFS(self,lxc,vgname="docklet-group"):
        rootfs = "/var/lib/lxc/%s/rootfs" % lxc
        layer = self.NFS_PREFIX + "/local/aufs" + lxc
        self.sys_call("mountpoint %s &>/dev/null && umount -l %s" % (rootfs,rootfs))
        self.sys_call("mountpoint %s &>/dev/null && umount -l %s" % (layer,layer))  
        self.sys_call("rm -rf /var/lib/lxc/%s" % lxc)
        self.sys_call("lvremove -f %s/%s" % (vgname,lxc))

    def checkFS(self,lxc,vgname="docklet-group"):
        rv = self.sys_return(self.srcpath+"lvmtool.sh check volume %s %s" % (vgname,lxc))
        if rv == 0:
            logger.info("lv %s exist" % lxc)
            return 0
        else:
            logger.info("lv %s not exist" % lxc)
            return 1

    def checkPOOL(self,vgname="docklet-group",fp="/opt/docklet/local/docklet-storage"):
        rv = self.sys_return(self.srcpath+"lvmtool.sh check group %s" % vgname)
        if rv == 1:
            logger.info("vg %s not exist" % vgname)
            return 1
        elif rv == 2:
            logger.info("loop file %s not exist" % fp)
            return 2
        else:
            logger.info("vg %s exist" % vgname)
            return 0

    def deletePOOL(self,vgname="docklet-group",fp="/opt/docklet/local/docklet-storage"):
        self.sys_call("vgremove -f %s" % vgname)
        self.sys_call("umount /dev/loop0")
        self.sys_call("losetup -d /dev/loop0")
        self.sys_call("rm -f %s" % fp)


    def removeImage(self,user,image):
        imgpath = self.imgpath + "private/" + user + "/"
        self.sys_call("rm -rf %s/" % imgpath+image)
        self.sys_call("rm -f %s" % imgpath+"."+image+".info")
        self.sys_call("rm -f %s" % (imgpath+"."+image+".description"))

    def shareImage(self,user,image):
        imgpath = self.imgpath + "private/" + user + "/"
        share_imgpath = self.imgpath + "public/" + user + "/"
        image_info_file = open(imgpath+"."+image+".info", 'r')
        [createtime, isshare] = image_info_file.readlines()
        isshare = "shared"
        image_info_file.close()
        image_info_file = open(imgpath+"."+image+".info", 'w')
        image_info_file.writelines([createtime, isshare])
        image_info_file.close()
        self.sys_call("mkdir -p %s" % (share_imgpath + image))
        self.sys_call("rsync -a --delete %s/ %s/" % (imgpath+image,share_imgpath+image))
        self.sys_call("cp %s %s" % (imgpath+"."+image+".info",share_imgpath+"."+image+".info"))
        self.sys_call("cp %s %s" % (imgpath+"."+image+".description",share_imgpath+"."+image+".description"))

        

    def unshareImage(self,user,image):
        public_imgpath = self.imgpath + "public/" + user + "/"
        imgpath = self.imgpath + "private/" + user + "/"
        if os.path.exists(imgpath + image):
            image_info_file = open(imgpath+"."+image+".info", 'r')
            [createtime, isshare] = image_info_file.readlines()
            isshare = "unshare"
            image_info_file.close()
            image_info_file = open(imgpath+"."+image+".info", 'w')  
            image_info_file.writelines([createtime, isshare])
            image_info_file.close()
        self.sys_call("rm -rf %s/" % public_imgpath+image)
        self.sys_call("rm -f %s" % public_imgpath+"."+image+".info")
        self.sys_call("rm -f %s" % public_imgpath+"."+image+".description")
        

    def get_image_info(self, user, image, imagetype):
        if imagetype == "private": 
            imgpath = self.imgpath + "private/" + user + "/"
        else:
            imgpath = self.imgpath + "public/" + user + "/"
        image_info_file = open(imgpath+"."+image+".info",'r')
        time = image_info_file.readline()
        image_info_file.close()
        image_description_file = open(imgpath+"."+image+".description",'r')
        description = image_description_file.read()
        image_description_file.close()
        if len(description) > 15:
            description = description[:15] + "......"
        return [time, description]

    def get_image_description(self, user, image):
        if image['type'] == "private":
            imgpath = self.imgpath + "private/" + user + "/"
        else:
            imgpath = self.imgpath + "public/" + image['owner'] + "/"
        image_description_file = open(imgpath+"."+image['name']+".description", 'r')
        description = image_description_file.read()
        image_description_file.close()
        return description

    def list_images(self,user):
        images = {}
        images["private"] = []
        images["public"] = {}
        imgpath = self.imgpath + "private/" + user + "/"
        private_images = self.sys_call("ls %s" % imgpath)
        if private_images is not None and private_images[:3] != "ls:":
            private_images = private_images.split("\n")
            for image in private_images:
                fimage={}
                fimage["name"] = image
                fimage["isshared"] = self.isshared(user,image)
                [time, description] = self.get_image_info(user, image, "private")
                fimage["time"] = time
                fimage["description"] = description
                images["private"].append(fimage)
        else:
            pass
        imgpath = self.imgpath + "public" + "/"
        public_users = self.sys_call("ls %s" % imgpath)
        if public_users is not None and public_users[:3] != "ls:":
            public_users = public_users.split("\n")
            for public_user in public_users:
                imgpath = self.imgpath + "public/" + public_user + "/"
                public_images = self.sys_call("ls %s" % imgpath)
                if public_images is not None and public_images[:3] != "ls:":
                    public_images = public_images.split("\n")
                    images["public"][public_user] = []
                    for image in public_images:
                        fimage = {}
                        fimage["name"] = image
                        [time, description] = self.get_image_info(public_user, image, "public")
                        fimage["time"] = time
                        fimage["description"] = description
                        images["public"][public_user].append(fimage)
        else:
            pass
        return images
    
    def isshared(self,user,image):
        imgpath = self.imgpath + "private/" + user + "/"
        image_info_file = open(imgpath+"."+image+".info",'r')
        [time, isshare] = image_info_file.readlines()
        image_info_file.close()
        if isshare == "shared":
            return "true"
        else:
            return "false"

if __name__ == '__main__':
    mgr = ImageMgr()
    if sys.argv[1] == "prepareImage":
        mgr.prepareImage(sys.argv[2],sys.argv[3],sys.argv[4])
    elif sys.argv[1] == "create":
        mgr.createImage(sys.argv[2],sys.argv[3],sys.argv[4])
    else:
        logger.warning("unknown option")
