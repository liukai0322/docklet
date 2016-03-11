## MPI 示例 ##

Docklet提供了 [MPICH2](http://www.mpich.org) 软件包。

假定vcluster目前有两个节点 host-0 和 host-1

进入 WEB Terminal。

```
$ cat /etc/hosts
127.0.0.1       localhost
172.16.0.46     host-0  host-0.tee
172.16.0.45     host-1  host-1.tee
```

获得节点列表 

```
$ cat /etc/hosts | grep -v localhost | awk '{print $2}'
host-0
host-1
```

WEB Terminal进入的是host-0，在host-0 上编辑 mpihello.c 

```c
#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>
#define  MASTER     0

int main (int argc, char *argv[])
{
    int   numtasks, taskid, len;
    char hostname[MPI_MAX_PROCESSOR_NAME];

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
    MPI_Comm_rank(MPI_COMM_WORLD,&taskid);
    MPI_Get_processor_name(hostname, &len);
    printf ("Hello from task %d on %s!\n", taskid, hostname);
    if (taskid == MASTER)
        printf("MASTER: Number of MPI tasks is: %d\n",numtasks);
    MPI_Finalize();
    return 0 ;
}
```

在WEB Terminal中运行:

```
$ mpicc mpihello.c -o mpihello
$ mpirun -n 2 -hosts host-0,host-1 mpihello
Hello from task 0 on host-0! 
MASTER: Number of MPI tasks is: 2 
Hello from task 1 on host-1!
```
