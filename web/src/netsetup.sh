#!/bin/bash

# netsetup.sh : setup network for docklet
# usage: netsetup.sh ACTION IP
#   ACTION: init -- init bridges
#           gre  -- setup GRE tunnel to remote ip
#   IP    : bridge ip if init, like 10.0.0.1/8
#           remote ip if gre, like 192.168.4.12
#
# Network Topology:
#                                     Worker
#          Master        +--------- docklet-br 
#                        |GRE
#        docklet-br -----+
#                        |GRE
#                        +--------- docklet-br
#                                     Worker

ACTION=$1

if [[ $ACTION == "init-withclean" ]];then
	IP=$2
	# clean bridges 
	if ip link show docklet-br &>/dev/null; then
		echo "[Warning] [netsetup.sh] docklet-br already exists. delete it"
		ip link set docklet-br down &>/dev/null
		# maybe docklet-br is created by brctl or ovs-vsctl 
		# now create by ovs-vsctl, but in old version, created by brctl
		brctl delbr docklet-br &>/dev/null
		ovs-vsctl del-br docklet-br &>/dev/null
		ip link show docklet-br &>/dev/null && echo "[Error] [netsetup.sh] delete docklet-br failed"
	fi
	# docklet-link is no use now. but maybe in use in old version. so we delete it here
	if ip link show docklet-link &>/dev/null; then
		echo "[Warning] [netsetup.sh] docklet-link already exists. delete it"
		ip link set docklet-link down &>/dev/null
		ovs-vsctl del-br docklet-link &>/dev/null
		ip link show docklet-link &>/dev/null && echo "[Error] [netsetup.sh] delete docklet-link failed"
	fi

	# create new bridges 
	# now we only use docklet-br. docklet-link is no need now
	echo "[Info] [netsetup.sh] create docklet-br"
	ovs-vsctl add-br docklet-br
	ip address add $IP dev docklet-br 
	ip link set docklet-br up
elif [[ $ACTION == "init" ]];then
	IP=$2
	if ip link show docklet-br &>/dev/null; then 
		echo "[Warning] [netsetup.sh] docklet-br already exists, reuse it. You should check its IP and configuration"
	else
		echo "[Info] [netsetup.sh] create docklet-br"
		ovs-vsctl add-br docklet-br
		ip address add $IP dev docklet-br
		ip link set docklet-br up
	fi
elif [[ $ACTION == "gre-withclean" ]];then
	IP=$2
	echo "[Info] [netsetup.sh] setup GRE tunnel ..."
	ovs-vsctl add-port docklet-br gre-$IP -- set interface gre-$IP type=gre options:remote_ip=$IP
elif [[ $ACTION == "gre" ]]; then
	IP=$2
	if [[ $(ovs-vsctl list-ports docklet-br | grep -P "^gre-$IP$") != "" ]]; then
		echo "[Info] [netsetup.sh] gre-$IP already exists, reuse it. Maybe you need to check its configuration"
	else
		echo "[Info] [netsetup.sh] setup GRE tunnel to $IP"
		ovs-vsctl add-port docklet-br gre-$IP -- set interface gre-$IP type=gre options:remote_ip=$IP
	fi
elif [[ $ACTION = "newgw" ]];then
	echo "[Info] [netsetup.sh] setup new GATEWAY $NAME"
	NAME=$2
	IP=$3
	ID=$4
	ovs-vsctl add-port docklet-br $NAME tag=$ID -- set interface $NAME type=internal
	ip address add $IP dev $NAME
	ip link set $NAME up
elif [[ $ACTION == "delgw" ]];then
	echo "[Info] [netsetup.sh] delete GATEWAY $NAME"
	NAME=$2
	ovs-vsctl del-port $NAME
else
	echo "[Error] [netsetup.sh] $ACTION is not supported"
fi
