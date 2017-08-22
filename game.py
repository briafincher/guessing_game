"""A number-guessing game."""
import random

print 'Hello there! What is your name?'
name = raw_input('Name: ')

number = random.randint(1, 100)
print number

while True:
    guess = int(raw_input('Pick a number between 1 and 100: '))
    if guess > number:
        print 'Too high!'
    elif guess < number:
        print 'Too low!'
    else:
        print 'Great job, {}!'.format(name)
        break
