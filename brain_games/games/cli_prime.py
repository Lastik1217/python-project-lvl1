#!/usr/bin/env python
import prompt
from random import randint
from brain_games.cli import a


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        x = randint(1, 50)
        Question = str(x)
        if x == 2:
            correct = 'yes'
        elif x == 3:
            correct = 'yes'
        elif x == 5:
            correct = 'yes'
        elif x == 7:
            correct = 'yes'
        elif x == 11:
            correct = 'yes'
        elif x == 13:
            correct = 'yes'
        elif x == 17:
            correct = 'yes'
        elif x == 19:
            correct = 'yes'
        elif x == 23:
            correct = 'yes'
        elif x == 29:
            correct = 'yes'
        elif x == 31:
            correct = 'yes'
        elif x == 37:
            correct = 'yes'
        elif x == 41:
            correct = 'yes'
        elif x == 43:
            correct = 'yes'
        elif x == 47:
            correct = 'yes'
        else:
            correct = 'no'
        print('Question: ' + Question)
        ans = input('Your answer: ')
        if ans == correct:
            print('Correct!')
            count += 1
        else:
            return(f"'{ans}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.\n Let's try again, {a}!")
            break
        if count == 3:
            return("Congratulations, " + a + "!")
#== 2 or 3 or 5 or 7 or 11 or 13 or 17 or 19 or 23 or 29 or 31 or 37 or 41 or 43 or 47