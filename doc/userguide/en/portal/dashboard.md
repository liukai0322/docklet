## Dashboard ##

Dashboard is where users manage their Workspaces. Users can view 
, create, start, stop,  delete and enter their Workspaces.   

Initially the Workspace list is empty. Users need to create a Workspace
first. Click on **Add Workspace** will enter the web page for creating
Workspace, then select the image, and create a Workspace named **tee**, as
illustrated as follows:

<img src="../images/workspace-create.png" width="600" alt="add 
workspace">

If the creation succeed, the Workspace list changed to:

<img src="../images/dashboard-stop.png" width="600" alt="dashboard
stopped status">

We can see a Workspace named **tee** has been created, with status **Stopped**.
Now the user can choose to **Start** or **Delete** the Workspace. 

The *Stopped* Workspace still exists and wait for next start. Users are
encouraged to stop their Workspace when not running jobs to reduce
resource consumption.

Now click **Start** to start the Workspace. The Workspace status changed
to:

<img src="../images/dashboard-start.png" width="600" alt="dashboard
running status">

The Workspace status is **Running**. Users can choose to  **Stop** the 
Workspace, or **Go** into the Workspace. They can also click the name
*tee* to [Config](config.md) the Workspace. If click on the status
**Running**, will show the detailed vcluster [Status](status.md).

**Note**: 

1. If the users click **Go** soon after creation of a Workspace,
they may get an error message of `503: Proxy Target Missing`, this is possibly 
because of the Workspace backend initialization not finished. Click
**Go** some time later, users will enter the Workspace as expected. 

2. If the users click **Go**, but get `Not Found`  error message:

```
Not Found

The requested URL was not found on the server. If you entered the URL
manually please check your spelling and try again.
```

It is possibily because the system has experiened a recovery. Users need to
manually reboot their Workspaces to gain access.
