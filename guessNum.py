## Guessing a random number game


import random

## use random library to store a random integer
## between 1-20
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20')

## Allow for 6 guesses
for guessesTaken in range(1, 7):
    print('Take a guess')
    
    # integer for user input
    guess = int(input())

    if guess < secretNumber:

        print('too low!')

    elif guess > secretNumber:
        print('too high')

    else:
        break # satisfied for loop (since number is neither too high or too low), breaks


if guess == secretNumber:
    print('Good guess! It took you '+str(guessesTaken) +' guesses')

else:
    print('The number I was thinking of was: '+str(secretNumber)+'')

