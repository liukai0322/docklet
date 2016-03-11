## vcluster ##

Vcluster(virtual cluster) is the basic concept in Docklet. A vcluster
consists of at least one LXC container nodes, each node can be regarded
as a lightweight Linux host. Usually, the container nodes of one
vcluster are generated from the same image, which can simplify the
management of vcluster. 

The level of the user determines the quota of his vcluster, including
the maximum number of nodes the vcluster can have, the CPU and memory
config of each container node, etc. The default vcluster has one node. 

The nodes of Docklet vcluster are designed to distribute to different
physical hosts as most as possible, in order to better utilize physical
resources. Those distributed nodes can communicate with each other. One
docklet vcluster will use an independent virtual sub-network, usually
the first node is the gateway of this sub-network.

In most cases, users do not need to care about the details of vcluster,
but only need to focus on their Workspace. 

In some special cases, users may need to configure the vcluster to meet
the requirements of upper Workspace.  For example, in order to run
program parallelly in Workspace, users need to scale out the default
vcluster, adding more nodes. Docklet vcluster has the ability of elastic
scaling, supporting adding or removing nodes at any time.
