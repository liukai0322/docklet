## WEB Terminal ##

To operate in terminal is necessary for many developers. Almost all
system administrator, programming, debugging and analyzing jobs can be
performed in terminal environment.

In the Jupyter Notebook dashboard, click **New** - **Terminal** will create a new WEB Terminal and then enter the terminal, where users can do their stuffs like editing a file using vi, running a program, etc.

The Jupyter Notebook WEB Terminal has one important feature: running in
the background, even users has closed the WEB Terminal webpage. The
user can find all their live Terminals by clicking **Running** -
**Terminals** in the dashboard. They can re-enter the Terminal by
clicking the name, to recover their work. This feature is very important
for long running jobs.

If the user re-enter the Terminal after a long period of idle time, the Terminal
may show no response to user input. Usually refresh the page will get it
back.

If the user will perform multiple tasks, they can open several
Terminals, or using [tmux](https://tmux.github.io) in one Terminal.

### Install Software ###

Users can install software packages not in the base image. The Docklet
container is based on Ubuntu. The command `apt-get` is used for package
installation.

Example:

```
$ apt-get install clang
```

Users are encouraged to clean the `apt-get` cache to save disk space

```
$ apt-get clean
```

About `apt-get`, please refer to
the [official help](https://help.ubuntu.com/community/AptGet/Howto).
