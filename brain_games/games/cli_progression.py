#!/usr/bin/env python
import prompt
from random import randint
from brain_games.welcome_cli import name
from brain_games.engine import count_games


def play_progress():
    print('What number is missing in the progression?')
    count = 0
    while count != count_games:
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
                  f"Correct answer was '{correct}'.\n Let's try again, {name}!")
            break
        if count == count_games:
            return("Congratulations, " + name + "!")
