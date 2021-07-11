#!/usr/bin/env python
import prompt
from random import randint
from brain_games.cli import a


def prog():
    print('What number is missing in the progression?')
    count = 0
    while count != 3:
        question = ''
        long_progr = randint(5, 10)
        min_prog = randint(1, 20)
        step = randint(2, 10)
        mask = randint(1, long_progr)
        for count_p in range(long_progr):
            min_prog = min_prog + step
            if count_p == mask:
                correct = min_prog
                question = question + ' ..'
            else:
                question = question + ' ' + str(min_prog)
        print('Question:' + question)
        answer = prompt.integer('Your answer: ')
        if answer == correct:
            print('Correct!')
            count += 1
        else:
            return(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.\n Let's try again, {a}!")
            break
        if count == 3:
            return("Congratulations, " + a + "!")
