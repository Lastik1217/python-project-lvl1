#!/usr/bin/env python
import prompt
from random import randint
from brain_games.welcome_cli import name
from brain_games.engine import count_games


def play_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != count_games:
        question = randint(2, 50)
        print('Question: ' + str(question))
        x = 0
        for i in range(2, question // 2 + 1):
            if question % i == 0:
                x = x + 1
        if (x <= 0):
            corr = 'yes'
        else:
            corr = 'no'
        answer = prompt.string('Your answer: ')
        if answer == corr:
            print('Correct!')
            count += 1
        else:
            return(f"'{answer}' is wrong answer ;(. "
                   f"Correct answer was '{corr}'.\n Let's try again, {name}!")
            break
        if count == count_games:
            return("Congratulations, " + name + "!")
