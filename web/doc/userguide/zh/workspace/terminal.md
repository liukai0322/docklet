## 终端操作 ##

终端(Terminal) 操作对于很多开发者来说是必需的，
在终端下几乎可以进行所有的系统管理、开发调试、运行分析任务。

在Jupyter Notebook工作面板中，
点击 **New** - **Terminal** 可以创建一个新Terminal并进入其中进行操作，
如调用 vi 编辑文件，运行程序等。

Jupyter Notebook的WEB Terminal有个很重要的特点：可以在后台运行。
即使用户在浏览器中关闭了 Terminal 页面，其仍然在后台运行。
用户可以在 Jupyter Notebook的工作面板 - **Running** - **Terminals**
中找到正在运行的 Terminal ，点击进入其中，恢复工作场景。
这对于长运行的作业很有意义。

如果长时间没有操作 Terminal，可能会出现操作无反应现象，
刷新页面通常即可激活。 

如果要执行多个任务，可以打开多个 Terminal，
也可以在一个 Terminal 中使用 [tmux](https://tmux.github.io) 。

### 安装软件包 ###

用户可以在WEB Terminal中安装软件包。基础系统是Ubuntu，用户使用 `apt-get`
命令进行安装。

```
$ apt-get install clang
```

如果用户希望未来将工作区保存为镜像，建议清除 `apt-get` 的缓存以减少空间
占用:

```
$ apt-get clean
```

有关`apt-get`，可参阅 
[帮助文档](https://help.ubuntu.com/community/AptGet/Howto)。
