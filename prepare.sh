#!/bin/bash

##################################################
#                before-start.sh
# when you first use docklet, you should run this script to
# check and prepare the environment
# *important* : you need run this script again and again till success
##################################################

if [[ "`whoami`" != "root" ]]; then
	echo "FAILED: Require root previledge !" > /dev/stderr
	exit 1
fi

# check cgroup control
which cgm &> /dev/null || { echo "FAILED : cgmanager is required, please install cgmanager" && exit 1; }
cpucontrol=$(cgm listkeys cpu)
[[ -z $(echo $cpucontrol | grep cfs_quota_us) ]] && echo "FAILED : cpu.cfs_quota_us of cgroup is not supported, you may need to recompile kernel" && exit 1
memcontrol=$(cgm listkeys memory)
if [[ -z $(echo $memcontrol | grep limit_in_bytes) ]]; then
	echo "FAILED : memory.limit_in_bytes of cgroup is not supported"
	echo "Try : "
	echo -e "  echo 'GRUB_CMDLINE_LINUX=\"cgroup_enable=memory swapaccount=1\"' >> /etc/default/grub; update-grub; reboot" > /dev/stderr
	echo "Info : if not success, you may need to recompile kernel"
	exit 1
fi

# install packages that docklet needs (in ubuntu)
# some packages' name maybe different in debian
apt-get install -y cgmanager lxc lvm2 bridge-utils curl exim4 openssh-server openvswitch-switch 
apt-get install -y python3 python3-netifaces python3-flask python3-flask-sqlalchemy
apt-get install -y python3-requests python3-suds
apt-get install -y nodejs nodejs-legacy npm
apt-get install -y etcd

# check and install configurable-http-proxy
which configurable-http-proxy &>/dev/null || npm install -g configurable-http-proxy

# prepare basefs of lxc
tempdir=/opt/docklet/local/temp

echo "Generating docklet.conf from template "
cp conf/docklet.conf.template conf/docklet.conf

echo "Try downloading basefsf.tar.bz to $tempdir"

[[ ! -d $tempdir ]] && mkdir -p $tempdir
if [[ ! -f $tempdir/basefs.tar.bz ]]; then
    echo "Downloading basefs.tar.bz to $tempdir"
	wget http://sei.pku.edu.cn:8000/download/basefs -O $tempdir/basefs.tar.bz
fi


echo ""

echo "All preparation installation is done."

echo ""

echo "NOTE: Please run dpkg-reconfigure exim4-config, just select internet site"

echo ""

echo "Then start docklet as described in README"
