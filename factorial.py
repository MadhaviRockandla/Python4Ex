"""
Exercise 5
Factorials are used to count permutations.
Create a program called factorial.py.
Requirements
Given a number (x), determine the value of x!
Use recursion
x		result
0!		1
1!	1 * 1	1
2!	2 * 1	2
3!	3 * 2 * 1	6
4!	4 * 3 * 2 * 1	24
5!	5 * 3 * 2 * 1	120
...	...	...
Constraints
n >= 0 n < 995

"""


def factorial(n):
    if n > 1:
        return factorial(n - 1) * n
    elif n == 0 or n == 1:
        return 1
    return factorial(n)


n = int(input("Give a number between 0 (include) and 995: "))
if 0 <= n < 995:
    print('Factorial of', n, 'is', factorial(n))
else:
    print("Please give a valid input")
