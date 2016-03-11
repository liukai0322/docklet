## Why to use Docklet ##

As a "**Workspace Cloud**", Docklet has several advantages.

First, what Docklet provides is a virtual workspace for developers, but
no only an Iaas or PaaS solution, therefore more friendly to deveopers.

Second, the Docklet vcluster provides a high effient and simple method
of sharing physical resources, therefore more friendly to
administrators.

The detailed advantages and features of Docklet include:

### Wide applicability ###

Docklet is not designed for large data center, but for small or **mini
data center**. By **mini data center**, we mean a cluster with not more than 100
physical hosts, all connected by high speed network, each host with
relatively high performance. This is the common configuration of most
medium or small enterprises and institutes. Therefore, Docklet has a
wide applicability.

### Easily Sharing Cluster among Frameworks ###

Traditionally clusters are often monopolized, serving only one kind of
application framework, e.g., MPI or Spark.  It is usually difficult to
share the physcal cluster among different frameworks.

[Mesos](http://mesos.apache.org) and
[Yarn](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html) each try to provide a mechanism of sharing clusters. However, they require extra work of customization for each supported framework, which seems not flexible and a bit difficult.

Docklet provides a flexible and easy solution. By virtualizing the
physical clusters, almost all computing frameworks can run in the
LXC vcluster seamlessly without any customization and modification.

### Dynamically and Elastically Configure Resources ###

Docklet vcluster supports elastically configuring resources. Users can
add a fully functional LXC node to existing vcluster instantly by just a
click. This feature is useful for the application frameworks that
support elastic resource management, e.g., Spark.

Docklet can monitor the activity of users, smartly finding those not at work, 
then adjust their resource quota dynamically. This can bring about good
usage experience for online active users, together with reasonable
resource utilization. 

### Consuming Very Few Network Resources ###

Docklet utilizes the technology of software defined networks. 
The inner vclusters will use private Internet address space, e.g.,
`172.16/16`, not consuming public Internet addresses. The administrator
only need to configure **one** public Internet address/URL for Docklet
portal.  Users use just a modern browser to access their private
vcluster located behind the enterprise's firewall through the portal's 
public URL. This feature is very attractive for those enterprises
without so many public Internet addresses.

### User Friendly ###

Docklet is mainly targeted for enterprises's staff developers. It is
domain oriented, therefore can be setup to meet the enterprise's
requirements deliberately. The public base image has most often used
software. Users can directly start their programming and analyzing job
with just a browser, without the heavy burden of installing and
configuring the physical clusters, installation of software frameworks, 
management of images, etc. Therefore, it is very friently to end users,
which is especially important for those non-export users.

### Ideal Environment for Application Development and Testing ###

The easy usage of Docklet means it can be an ideal environment for
application development and testing. For example, users can program and
debug a big data analyzing software with a small data set (possibly
Gigabye scale). If success, then deploy it to production system with
true big data. In fact, for most data analyzing and mining jobs, their
data set is usually not so large, which means they can directly run and
output the final results in Docklet.

Docklet is also a good platform for exercising programming skills and
studying programming languages. No need to install kinds of tools, just
a browser is OK.

### Easy to Customize and Extend ###

The enterprise's Docklet administrator is free to make specific public base
images. The users can also install new software not in the base image.
What is more, the users can save their Workspace as image and then share
with others, which is very convenient for users of one group.

### Supporting Multiple Users ###

Docklet vcluster naturally supports multiple users. Each user has their
own private vcluster independenlty.  Each vcluster can run different
frameworks such as MPI and Spark without worry about interference.
Therefore, it can satisfy the different requirements of different users.

### Advantages of LXC ###

Docklet uses LXC technology. Therefore, it has the advantages of LXC and
LXC-based solutions like Docker, including instant booting container in seconds;
high utilization of resources, running thousands of containers in one
physical host; high performance of applications; consuming less
resources; fast delivery; simple management, etc.
