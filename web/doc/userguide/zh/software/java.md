## Java 

Docklet 提供了 OpenJDK 7+，用于开发Java程序。

一个计算阶乘的Java程序 NumberFactorial.java 如下:

```java
public class NumberFactorial {
    public static void main(String[] args) {
        int number = 5;
        /*
         * Factorial of any number is !n.
         * For example, factorial of 4 is 4*3*2*1.
         */

        int factorial = number;

        for(int i =(number - 1); i > 1; i--) {
            factorial = factorial * i;
        }

        System.out.println("Factorial of a number is " + factorial);
    }
}
```

进入 WEB Terminal，编译运行 

```
$ javac NumberFactorial.java
$ java NumberFactorial
Factorial of a number is 120
```

