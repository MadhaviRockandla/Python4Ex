"""
Exercise 2
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Given the term n, determine the value of x(n).

| | | | | | | | | | | | | | | | ------- | - | - | - | - | - | - | - | -- | -- | -- | -- | -- | -- | | n = | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | .. | | x(n) = | 0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | .. |

When n = 0, x(n) = 0
When n = 4, x(n) = 3
When n = 5, x(n) = 5

x(n) can be determined with the following rule:
x(n) = x(n - 1) + x(n - 2)

Create a program called fibonacci_recursive.py

Requirements

Given a term (n), determine the value of x(n).
In the fibonacci_recursive.py program, create a function called fibonnaci. The function should take in an integer and return the value of x(n).
This problem must be solved using recursion.
Constraints
n >= 0 and n <= 30
"""


def fibonacci(n):
    if n < 0:
        print("wrong input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n >= 3 and n <= 30:
        return fibonacci(n - 1) + fibonacci(n - 2)
    else:
        print("wrong input")


print(fibonacci(30))
