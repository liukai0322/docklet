## Java Example ##

Docklet provides OpenJDK 7+ to develop Java program.

`NumberFactorial.java` is to calculate factorial of `n`: 

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

Open WEB Terminal, compile and run 

```
$ javac NumberFactorial.java
$ java NumberFactorial
Factorial of a number is 120
```
