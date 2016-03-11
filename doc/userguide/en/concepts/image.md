## Image ##

The concept of image in Docklet is similar to that in [Docker](https://github.com/docker/docker), i.e., a readonly template to create containers. But there are some differences.

Since Docker mainly focuses on LXC container in IaaS level, its images are 
very free and versatile.  Users can customize and make their own images
and then upload them to the docker hub.  Usually one Docker image has
only the environment of one specific application. For example, a Docker
image may have a full Ubuntu operating environment,  in which there is
only the Apache web server software.

Docklet is a bit different. Docklet focuses on **Workspace** and
**vcluster**, therefore has special restrictions about images, not
supporting uploading user-made images. The Docklet administrator will
make one or more public base image according to the common requirements
of the enterprise, containing the needed software packages to support
Workspace, together will some programming tools and frameworks such as
MPI, Spark, Python and R. Since the Docklet public base images are
shared by all users, therefore is usually larger than typical Docker
containers.

If users can not find needed software tools in the public base image,
they can install them in their Workspace. They can then save their
Workspace as private image, and can choose to share it with others.
