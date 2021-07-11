#!/usr/bin/env python
from random import randint
from brain_games.cli import a


def ask_a_question():
    count = 0
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while count != 3:
        x = randint(0, 50)
        if x % 2 == 0:
            cor_ans = "'yes'"
        else:
            cor_ans = "'no'"
        print('Question: ' + str(x))
        ans = input('Your answer: ')
        if ans == 'yes' and x % 2 == 0 or ans == 'no' and x % 2 > 0:
            count += 1
            print('Correct!')
        else:
            return(f"'{ans}' is wrong answer ;(. "
                  f"Correct answer was '{cor_ans}'.\n Let's try again, {a}!")
            break
        if count == 3:
            return("Congratulations, " + a + "!")
