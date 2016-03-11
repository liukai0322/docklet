## C/C++ 开发示例 ##

Docklet提供了GCC 5+ 和 GDB，用于帮助开发 C 程序。

### C

文件 `sum.c` 如下:

```c
#include <stdio.h>
#define TOP 50

int main()
{
    int i = 0 , sum = 0 ;
    while ( i <= TOP ) {
        sum += i ;
        i++ ;
    }
    printf(" Sum of 1 to %d is %d\n", TOP, sum ) ;
    return 0 ;
}
```

进入WEB Terminal，编译并运行 

```
$ gcc -g sum.c -o sum
$ ./sum
 Sum of 1 to 50 is 1275
```

### C++

下面显示了一个有错的C++程序`main.cpp`，原文来源于[这里](http://www.cprogramming.com/gdb.html)

```c++
#include<iostream>
 
using namespace std;
 
long factorial(int n);
 
int main()
{
    int n(0);
    cin>>n;
    long val=factorial(n);
    cout<<val;
    cin.get();
    return 0;
}
 
long factorial(int n)
{
    long result(1);
    while(n--)
    {
        result*=n;
    }
    return result;
}
```

进入 WEB Terminal，编译并运行，输入 5 ，结果 0
```
$ g++ -g main.cpp -o main
$ ./main
5
0
```

用gdb进行调试 
```
$ gdb ./main
1.      $ g++ main.cpp -g -Wall -o main
2.      $ gdb main
3.      GNU gdb (Ubuntu 7.10.1-0ubuntu1) 7.10.1
4.      Copyright (C) 2015 Free Software Foundation, Inc.
5.      This GDB was configured as "i686-redhat-linux-gnu".
6.      For bug reporting instructions, please see:
7.      <http://www.gnu.org/software/gdb/bugs/>...
8.      Reading symbols from /root/main...done.
9.      (gdb) break 11
10.     Breakpoint 1 at 0x80485f9: file main.cpp, line 11.
11.     (gdb) run
12.     Starting program: /root/main
13.     3
14.     
15.     Breakpoint 1, main () at main.cpp:11
16.     11        long val=factorial(n);
17.     (gdb) step
18.     factorial (n=3) at main.cpp:19
19.     19        long result(1);
20.     (gdb) list
21.     14        return 0;
22.     15      }
23.     16
24.     17      long factorial(int n)
25.     18      {
26.     19        long result(1);
27.     20        while(n--)
28.     21        {
29.     22          result*=n;
30.     23        }
31.     (gdb) watch n
32.     Hardware watchpoint 2: n
33.     (gdb) watch result
34.     Hardware watchpoint 3: result
35.     (gdb) continue
36.     Continuing.
37.     Hardware watchpoint 3: result
38.     
39.     Old value = 0
40.     New value = 1
```

`result` 变量初始化为1。

```
41.     factorial (n=3) at main.cpp:20
42.     20        while(n--)
43.     (gdb)
```

注意刚才没有输入任何命令，只是输入**回车**，它会重复执行上一条命令。

```
44.     Continuing.
45.     Hardware watchpoint 2: n
46.     
47.     Old value = 3
48.     New value = 2
```

注意 `n` 从 3 变成了 2.

```
49.     0x08048654 in factorial (n=2) at main.cpp:20
50.     20        while(n--)
51.     (gdb)
52.     Continuing.
53.     Hardware watchpoint 3: result
54.     
55.     Old value = 1
56.     New value = 2
```

此时 `result`变成了 2。我们已经发现了一个bug: `result`最终的值应为 `3*2*1`，
但这里只是从 2 开始计算，问题出在 `while (n--)`上。 

将代码修改为如下

```c++
while(n>0) //doesn't let n reach 0
{
  result*=n;
  n--;        //decrements only after the evaluation
}
```

测试运行通过。

[原文](http://www.cprogramming.com/gdb.html) 给出了更详细的调试过程。

GDB的官方手册请参考
[GDB手册](http://sourceware.org/gdb/current/onlinedocs/gdb/)。
