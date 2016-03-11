#!/bin/bash

# lvmtool.sh : tools for create lvm group, create lvm volume and check group or volume
#     create group   :   lvmtool.sh new group GROUP_NAME SIZE FILE_PATH
#     create volume  :   lvmtool.sh new volume GROUP_NAME VOLUME_NAME SIZE
#     check group :      lvmtool.sh check group GROUP_NAME
#     check volume :     lvmtool.sh check volume GROUP_NAME VOLUME_NAME
#     delete volume  :   lvmtool.sh delete volume GROUP_NAME VOLUME_NAME
#     delete group   :   lvmtool.sh delete group GROUP_NAME
#     recover group  :   lvmtool.sh recover group GROUP_NAME FILE_PATH 

ACTION=$1
TYPE=$2

if [[ $ACTION == 'new' && $TYPE == 'group' && $STORAGE == 'file' ]];then
	GROUP_NAME=$3
	SIZE=$4
	FILE_PATH=$5
	echo "[Info] [lvmtool.sh] begin initialize lvm group:$GROUP_NAME with size ${SIZE}M"
	# clean vg, device and loop file
	vgdisplay $GROUP_NAME &>/dev/null && echo "[Warnning] [lvmtool.sh] lvm group $GROUP_NAME already exists, delete it" && vgremove -f $GROUP_NAME 
	vgdisplay $GROUP_NAME &>/dev/null && echo "### delete VG failed"
	pvdisplay /dev/loop0 &>/dev/null && pvremove -ff /dev/loop0 
	pvdisplay /dev/loop0 &>/dev/null && echo "### remove pv failed"
	losetup /dev/loop0 &>/dev/null && echo "[Warnning] [lvmtool.sh] /dev/loop0 already exists, detach it" && losetup -d /dev/loop0 
	losetup /dev/loop0 &>/dev/null && echo "### losetup -d failed"
	[ -f $FILE_PATH ] && echo "[Warning] [lvmtool.sh] $FILE_PATH for lvm group already exists, delete it" && rm $FILE_PATH
	[ ! -d ${FILE_PATH%/*} ] && mkdir -p ${FILE_PATH%/*}
	dd if=/dev/zero of=$FILE_PATH bs=1M seek=$SIZE count=0 &>/dev/null
	losetup /dev/loop0 $FILE_PATH
	vgcreate $GROUP_NAME /dev/loop0
	echo "[Info] [lvmtool.sh] initialize lvm group:$GROUP_NAME with size ${SIZE}M success"
	exit 0

elif [[ $ACTION == 'recover' && $TYPE == 'group' && $STORAGE == 'file' ]];then
	GROUP_NAME=$3
	FILE_PATH=$4
	[ ! -f $FILE_PATH ] && echo "[Error] [lvmtool.sh] $FILE_PATH not found, unable to recover VG" && exit 1 
	losetup /dev/loop0 &>/dev/null || losetup /dev/loop0 $FILE_PATH
	losetup /dev/loop0 &>/dev/null || { echo "[Error] [lvmtool.sh] losetup failed"; exit 1; }
	sleep 1
	vgdisplay $GROUP_NAME &>/dev/null || vgcreate $GROUP_NAME /dev/loop0
	vgdisplay $GROUP_NAME &>/dev/null || { echo "[Error] [lvmtool.sh] create VG failed"; exit 1; } 
	echo "[Info] [lvmtool.sh] recover VG $GROUP_NAME success"
	exit 0

elif [[ $ACTION == 'new' && $TYPE == 'group' && $STORAGE == 'disk' ]];then
	GROUP_NAME=$3
	PV_NAME=$DISK
	echo "[Info] [lvmtool.sh] begin initialize lvm group:$GROUP_NAME with size ${SIZE}M"
	# clean vg, device and loop file
	vgdisplay $GROUP_NAME &>/dev/null && echo "[Warnning] [lvmtool.sh] lvm group $GROUP_NAME already exists, delete it" && vgremove -f $GROUP_NAME 
	vgdisplay $GROUP_NAME &>/dev/null && echo "### delete VG failed"
	vgcreate $GROUP_NAME $PV_NAME
	echo "[Info] [lvmtool.sh] initialize lvm group:$GROUP_NAME with size ${SIZE}M success"
	exit 0

elif [[ $ACTION == 'recover' && $TYPE == 'group' && $STORAGE == 'disk' ]];then
	GROUP_NAME=$3
	vgdisplay $GROUP_NAME &>/dev/null || vgcreate $GROUP_NAME /dev/loop0
	vgdisplay $GROUP_NAME &>/dev/null || { echo "[Error] [lvmtool.sh] create VG failed"; exit 1; } 
	echo "[Info] [lvmtool.sh] recover VG $GROUP_NAME success"
	exit 0

elif [[ "$ACTION" == "new" && $TYPE == "volume"  ]]; then
	GROUP_NAME=$3
	VOLUME_NAME=$4
	SIZE=$5
	lvdisplay $GROUP_NAME/$VOLUME_NAME &>/dev/null && echo "[Warnning] [lvmtool.sh] logical volume already exists, delete it" && lvremove -f $GROUP_NAME/$VOLUME_NAME
	lvcreate -L ${SIZE}M -n $VOLUME_NAME $GROUP_NAME
	echo "[Info] [lvmtool.sh] create lv for $LXC_NAME success"
	exit 0

elif [[ "$ACTION" == "check" && $TYPE == "group" ]]; then
	GROUP_NAME=$3
	vgdisplay $GROUP_NAME &>/dev/null && echo "[Info] [lvmtool.sh] check group $GROUP_NAME : exist" && exit 0
	echo "[Info] [lvmtool.sh] check group $GROUP_NAME : not exist" && exit 1
elif [[ $ACTION == "check" && "$TYPE" == "volume" ]]; then
	GROUP_NAME=$3
	VOLUME_NAME=$4
	lvdisplay $GROUP_NAME/$VOLUME_NAME &>/dev/null && echo "[Info] [lvmtool.sh] check volume $GROUP_NAME/$VOLUME_NAME : exist" && exit 0
	echo "[Info] [lvmtool.sh] check volume $GROUP_NAME/$VOLUME_NAME : not exist" && exit 1
elif [[ $ACTION == 'delete' && $TYPE == 'group' ]]; then
	GROUP_NAME=$3
	VOLUME_NAME=$4
	vgdisplay $GROUP_NAME &>/dev/null && vgremove -f $GROUP_NAME && exit 0
elif [[ $ACTION == 'delete' && $TYPE == 'volume' ]]; then
	GROUP_NAME=$3
	VOLUME_NAME=$4
	lvdisplay $GROUP_NAME/$VOLUME_NAME &>/dev/null && lvremove -f $GROUP_NAME/$VOLUME_NAME && exit 0
else
	echo "[Error] [lvmtool.sh] $ACTION $TYPE not supported" && exit 1
fi
