
"""Exercise 1
Create a program called fizz_buzz.py

The program should meet the following criteria.

The program prints each number from 1 to 100 to a new line.
If the number is a multiple of 3, print "Fizz" instead of the number.
If the number is a multiple of 5, print "Buzz" instead of the number.
If the number is a multiple of both 3 and 5, print "FizzBuzz" instead of the number.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)
