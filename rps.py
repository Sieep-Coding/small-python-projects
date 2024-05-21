# Rock, Paper, Scissors.

import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0

losses = 0

ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Choose [r]ock, [p]aper, [s]cissors, or [q]uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
         break
        print('type one of r, s, p, or q')
    if playerMove == 'r':
        print("ROCK versus...")
    elif playerMove == 'p':
        print("PAPER versus...")
    elif playerMove == 's':
        print("SCISSORS versus...")
    
    computerMove = random.choice(['r', 's', 'p'])

    if computerMove == 'r':
        print("ROCK")
    elif computerMove == 'p':
        print("PAPER")
    elif computerMove == 's':
        print('SCISSORS')
    if playerMove == computerMove:
        print("tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You Lose!")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You win!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1

        