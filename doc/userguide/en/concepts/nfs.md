## Dataspace ##

In Docklet, each user has their own persistent Dataspace, in which to
save data files. Dataspaces are isolated from each other, each user can
only visit their own Dataspace.

User's Dataspace is shared among all nodes of their vcluster. It is
located in the `~/nfs` directory of the container node. 

When the user save their Workspace as image, the Dataspace will be
excluded.

The Dataspace is supported by distributed file system in the backend.
Except the Dataspace, all data in containers will be destroyed as 
the containers are deleted. But the data in Dataspace will be persistent
regardless of the lifecycle of containers.

Users are encouraged to download and backup their important data in
time.
