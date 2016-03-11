## 什么是 Docklet ##

### 定义与结构 ###

Docklet 是北京大学软件工程研究所的一个开源项目，遵从 [新BSD 协议](http://directory.fsf.org/wiki/License:BSD_3Clause)，项目代码在 GitHub 
上进行维护。

Docklet的目标是实现一种**云化的个人工作区**解决方案，
使企业可以轻松地虚拟化其数据中心，为用户创建个人的虚拟集群，
进而为用户提供一个在**云端**的可定制工作区(Workspace)。 
用户只需要一个浏览器，即可随时随地访问企业内部自己的工作区，
在线进行代码编写、调试运行、数据管理、数据分析、结果可视化等工作。

Docklet的核心是基于Linux容器（LXC）技术和软件定义网络技术的容器集群。
它在LXC的基础上进行了进一步的封装，让用户不仅不需要关心单个容器的管理细节，
更无须关注各个分布容器之间的网络通信。
这样一个容器集群提供了一种物理集群虚拟化方案，
支持安装运行绝大多数已有的单机或分布式Linux应用，形成个人的开发工作区。
用户通过Docklet集成的[Jupyper Notebook](https://github.com/jupyter/notebook)
访问自己的工作区，通过浏览器完成开发运行等工作。


Docklet的结构如下图所示:

<img src="../images/docklet-architecture.jpg" width="500"
alt="docklet-architecture">

<!--
![docklet architecture](../images/docklet-architecture.jpg)
-->

### Docklet与Docker ###

Docklet和[Docker](https://github.com/docker/docker) 没有直接关系，
它们是两个完全不同的项目，设计目标也完全不同。

Docker的目标是实现轻量级的操作系统虚拟化解决方案，
位于云计算的[IaaS层](https://en.wikipedia.org/wiki/Cloud_computing)。
Docker在LXC的基础上进行了进一步的封装，
使得[用户操作 Docker 的容器就像操作一个快速轻量级的虚拟机一样简单
](https://www.gitbook.com/book/yeasy/docker_practice)。
虽然其后增加了网络集群能力，但本质上仍然是面向单机系统的，
位于软件栈的操作系统层。

Docklet的目标是实现一种开发者工作区的云化解决方案，
涵盖[SaaS、PaaS和IaaS层](https://en.wikipedia.org/wiki/Cloud_computing)。
Docklet的基础是LXC容器集群而不是Docker。
对Docklet用户而言，他们直接通过浏览器进行软件开发、调试
测试工作，面向的是运行于虚拟集群中的各种开发工具，这些工具处于软件栈的应用层。
