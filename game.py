"""A number-guessing game."""
import random


def play_game():
    number = random.randint(1, 100)
    print number

    num_guesses = 0
    guess = 0

    while num_guesses < 10:
        num_guesses += 1

        try:
            guess = int(raw_input('Pick a number between 1 and 100: '))
        except ValueError:
            print "Sorry, you must choose an integer!"
            continue

        if guess < 1 or guess > 100:
            print 'That is not a valid number. Enter a number between 1 and 100.'
        elif guess > number:
            print 'Too high!'
        elif guess < number:
            print 'Too low!'
        else:
            print 'Great job, {}! You found my number in {} guesses.'.format(name, num_guesses)
            break
    if num_guesses >= 10:
        print 'Too many tries!'
    return num_guesses

print 'Hello there! What is your name?'
name = raw_input('Name: ')

score1 = play_game()
best_score = score1
if score1 < 10:
    print 'Your best score is {}.'.format(best_score)

while True:
    new_game = raw_input('Do you wanna play another round?: ')
    if new_game == 'yes':
        score = play_game()
        if best_score > score:
                best_score = score
        print "Your best score is {}".format(best_score)
    else:
        break
