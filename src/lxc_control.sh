#!/bin/bash

# lxc_control.sh : start/stop a container
# usage : lxc_control.sh command lxc-name [ username clusterid hostname ip ]
# 1. lxc_control.sh create LXC_NAME USERNAME CLUSTERID HOSTNAME IP 
# 2. lxc_control.sh start LXC_NAME
# 3. lxc_control.sh stop LXC_NAME
# 4. lxc_control.sh delete LXC_NAME

CMD=$1
LXC_NAME=$2   # now lxc_name : username-clusterid-nodeid, maybe change later
USERNAME=$3
CLUSTERID=$4
HOSTNAME=$5   
IP=$6
GATEWAY=$7
VLANID=$8

# FS_PREFIX, DOCKLET_HOME, DOCKLET_LIB, ... are all set in python
[ -z $FS_PREFIX ] && FS_PREFIX="/opt/docklet"
[ -z $CONTAINER_CPU ] && CONTAINER_CPU=100000
[ -z $CONTAINER_MEMORY ] && CONTAINER_MEMORY=1000
[ -z $CONTAINER_DISK ] && CONTAINER_DISK=1000

[ -z $DOCKLET_LIB ] && echo "[lxc_control.sh] DOCKLET_LIB is null" && exit 1
[ -z $DOCKLET_CONF ] && echo "[lxc_control.sh] DOCKLET_CONF is null" && exit 1
[ -z $LXC_SCRIPT ] && echo "[lxc_control.sh] LXC_SCRIPT is null" && exit 1

LXCPATH=/var/lib/lxc/$LXC_NAME
ROOTFS=/var/lib/lxc/$LXC_NAME/rootfs
LAYER=$FS_PREFIX/local/volume/$LXC_NAME
CONFIG=/var/lib/lxc/$LXC_NAME/config

if [[ "$CMD" == "create" ]]; then
	[ ! -d $FS_PREFIX/global/users/$USERNAME ] && echo "[lxc_control.sh] user $USERNAME directory not found" && exit 1

	mkdir -p /var/lib/lxc/$LXC_NAME
	# gen config for container
	echo "[lxc_control.sh] generate config file for $LXC_NAME"
	sed -e "s|%ROOTFS%|$ROOTFS|g" \
		-e "s|%HOSTNAME%|$HOSTNAME|g" \
		-e "s|%IP%|$IP|g" \
		-e "s|%GATEWAY%|$GATEWAY|g" \
		-e "s|%CONTAINER_MEMORY%|$CONTAINER_MEMORY|g" \
		-e "s|%CONTAINER_CPU%|$CONTAINER_CPU|g" \
		-e "s|%FS_PREFIX%|$FS_PREFIX|g" \
		-e "s|%USERNAME%|$USERNAME|g" \
		-e "s|%CLUSTERID%|$CLUSTERID|g" \
		-e "s|%LXCSCRIPT%|$LXC_SCRIPT|g" \
		-e "s|%LXCNAME%|$LXC_NAME|g" \
		-e "s|%VLANID%|$VLANID|g" \
		$DOCKLET_CONF/container.conf > $CONFIG

	# *************************************************************
	# *** prepare rootfs, this maybe move to imagemgr.py later  ***
	# *** and it should be called in container.py , not here    ***
	# *************************************************************
	# clean ROOTFS and LAYER
	mountpoint $ROOTFS &>/dev/null && echo "[lxc_control.sh] $ROOTFS not clean"  && umount -l $ROOTFS 
	mountpoint $LAYER &>/dev/null && echo "[lxc_control.sh] $LAYER not clean" && umount -l $LAYER 
	rm -rf $ROOTFS $LAYER &>/dev/null
	mkdir -p $ROOTFS $LAYER &>/dev/null
	# get lvm volume for container
	if $DOCKLET_LIB/lvmtool.sh check volume docklet-group $LXC_NAME; then
		echo "[lxc_control.sh] volume $LXC_NAME already exists, delete it"
		$DOCKLET_LIB/lvmtool.sh delete volume docklet-group $LXC_NAME
	fi
	mkdir -p $LAYER/upper
	#mkdir -p $LAYER/{upper,work}
	$DOCKLET_LIB/lvmtool.sh new volume docklet-group $LXC_NAME $CONTAINER_DISK
	mkfs.ext4 /dev/docklet-group/$LXC_NAME &>/dev/null
	mount /dev/docklet-group/$LXC_NAME $LAYER/upper
	# overlay : should add overlay module in kernel -- modprobe overlay
	# lowerdir:ro, upperdir:rw
	# workdir: an empty dir with the same filesystem with upperdir
	#          needed by overlay, not used by us
	#mount -t overlay overlay -olowerdir=$FS_PREFIX/local/basefs,upperdir=$LAYER/upper,workdir=$LAYER/work $ROOTFS

	echo "[lxc_control.sh] create $LXC_NAME success with CONFIG:$CONFIG and ROOTFS:$ROOTFS"

	#mkdir -p ${LAYER}/etc
	#for DNS in ${DNS_SERVERS}; do echo "nameserver $DNS" > ${LAYER}/etc/resolv.conf; done
	
elif [[ $CMD == "start" ]]; then
	[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && echo "[lxc_control.sh] $LXC_NAME running, restart it" && lxc-stop -k -n $LXC_NAME
	#lxc-start -d -n $LXC_NAME -f /var/lib/lxc/$LXC_NAME/config -- /init
	#lxc-start -d -n $LXC_NAME -l INFO -f  /var/lib/lxc/$LXC_NAME/config -- /bin/bash /home/init
	lxc-start -d -n $LXC_NAME -l INFO -f  /var/lib/lxc/$LXC_NAME/config
	[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && echo "[lxc_control.sh] start $LXC_NAME success" && exit 0
	echo "[lxc_control.sh] start $LXC_NAME failed" && exit 1

# status of container : 0--running , 1--stopped
elif [[ $CMD == "status" ]]; then
	[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && exit 0
	exit 1

elif [[ $CMD == "check" ]]; then
	$DOCKLET_LIB/lvmtool.sh check volume docklet-group $LXC_NAME || { echo "[lxc_control.sh] check lv for $LXC_NAME failed, lv not found"; exit 1; }
	[ -d $LAYER/upper ] || mkdir -p $LAYER/{upper,work} &>/dev/null
	mountpoint $LAYER/upper &>/dev/null || mount /dev/docklet-group/$LXC_NAME $LAYER/upper
	#mountpoint $ROOTFS &>/dev/null || mount -t overlay overlay -olowerdir=$FS_PREFIX/local/basefs,upperdir=$LAYER/upper,workdir=$LAYER/work $ROOTFS
	mountpoint $ROOTFS &>/dev/null || mount -t aufs -o br=$LAYER/upper=rw:$FS_PREFIX/local/basefs=ro+wh none $ROOTFS
	echo "[lxc_control.sh] check $LXC_NAME : success" && exit 0

elif [[ $CMD == "recover" ]]; then
	[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && echo "[lxc_control.sh] recover: already running" && exit 0
	lxc-start -f $CONFIG -n $LXC_NAME 
	[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && echo "[lxc_control.sh] recover $LXC_NAME success" && exit 0
	echo "[lxc_control.sh] recover $LXC_NAME failed" && exit 1

elif [[ "$CMD" == "stop" ]]; then
	if [ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ]; then
		lxc-stop -k -n $LXC_NAME || true
	fi
	[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && echo "[lxc_control.sh] stop $LXC_NAME failed" && exit 1
	echo "[lxc_control.sh] stop $LXC_NAME success" && exit 0
elif [[ $CMD == "delete" ]]; then
	#[ "$(lxc-info -n $LXC_NAME -s 2>/dev/null | grep RUNNING)" != "" ] && echo "[lxc_control.sh] $LXC_NAME is still running, need to stop it fisrt" && exit 1
	lxc-stop -k -n $LXC_NAME
	# ******************************************************************
	# * below should be moved into imagemgr.py
	# * and should be called in container.py
	# ******************************************************************
	mountpoint $ROOTFS &>/dev/null && umount -l $ROOTFS
	mountpoint $LAYER/upper &>/dev/null && umount -l $LAYER/upper
	{ mountpoint $ROOTFS || mountpoint $LAYER/upper ; } && echo "[lxc_control.sh] umount failed"
	$DOCKLET_LIB/lvmtool.sh check volume docklet-group $LXC_NAME && $DOCKLET_LIB/lvmtool.sh delete volume docklet-group $LXC_NAME
	rm -rf $LAYER $LXCPATH
else
	echo "[lxc_control.sh] $CMD not supported"
	exit 1
fi



