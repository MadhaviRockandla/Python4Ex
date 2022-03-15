"""
Exercise 3
Create a program called fibonacci_linear.py

Requirements

Given a term (n), determine the value of x(n).
In the fibonacci_linear.py program, create a function called fibonnaci. The function should take in an integer and return the value of x(n).
This problem must be solved WITHOUT the use of recursion.
Constraints
n >= 0

"""

n = int(input("Give a number greater than or equal to 0: "))

def fibonacci(n):
    value_one = 0
    value_two = 1

    if n >= 0:
        for i in range(1, n, 1):
            result = value_one + value_two
            value_one = value_two
            value_two = result
        print(result)
    else:
        print("Please give a valid number")


if n >= 0 and n <= 30:
    fibonacci(n)
else:
    print("Please give a valid number")