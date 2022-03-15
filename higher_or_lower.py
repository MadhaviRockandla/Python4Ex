"""
Create a copy of the program called higher_or_lower.py from exercise 2 in Part 3.

Extend the functionality to meet the following requirements:

If a user's guess is incorrect, they get to keep guessing until they get it right.

"""


def guess_function():
    guess = input('Guess a number between 0 and 10: ')
    return int(guess)


def randnum_function():
    from random import randrange
    return randrange(10)


def evaluate():
    guess_number = guess_function()
    rand_number = randnum_function()
    if guess_number > rand_number:
        result = 'Number is Too High Please try another number'
        print('The random number was ' + str(rand_number) + '\n' + 'The guessed number was ' + str(
            guess_number) + '\n' + str(result))
        evaluate()
    elif guess_number < rand_number:
        result = 'Number is Too low Please try another number'
        print('The random number was ' + str(rand_number) + '\n' + 'The guessed number was ' + str(
            guess_number) + '\n' + str(result))
        evaluate()
    else:
        result = 'Equal'
    print('The random number was ' + str(rand_number))
    print('The number guessed was ' + str(guess_number))
    print('Your guess was ' + str(result) + 'Your are correct')


evaluate()
