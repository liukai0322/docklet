## C/C++ Example##

Docklet provides GCC 5+ and  GDB to help develop C program.

### C

Below is the source code of file `sum.c`:

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

Open WEB Terminal, compile and run 

```
$ gcc -g sum.c -o sum
$ ./sum
 Sum of 1 to 50 is 1275
```

### C++ ###

The following is a C++ program with bugs from [here](http://www.cprogramming.com/gdb.html).

The buggy `main.cpp`:

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

Open WEB Terminal, compile and run: input 5  and get wrong result 0.
```
$ g++ -g main.cpp -o main
$ ./main
5
0
```

Now debug with gdb 
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

Var `result` is initialized to 1.

```
41.     factorial (n=3) at main.cpp:20
42.     20        while(n--)
43.     (gdb)
```

Note that no commands are put here, just <return> is hit. 
It re-executes the last command.

```
44.     Continuing.
45.     Hardware watchpoint 2: n
46.     
47.     Old value = 3
48.     New value = 2
```

Now `n` is immediately decremented from 3 to 2.

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

Now result becomes 2 (by multiplying result's earlier value with n's
value). We've found the first bug! result is supposed to be evaluated by
multiplying 3 * 2 * 1 but here the multiplication starts from 2. To
correct it, we have to change the loop a bit.

```c++
while(n>0) //doesn't let n reach 0
{
  result*=n;
  n--;        //decrements only after the evaluation
}
```

After applying the fix, the test is passed.

[Here](http://www.cprogramming.com/gdb.html) describes the full
debugging process.

For how to use GDB, please reference the official
[GDB manual](http://sourceware.org/gdb/current/onlinedocs/gdb/)。
