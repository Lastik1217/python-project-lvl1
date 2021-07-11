#!/usr/bin/env python
import prompt
from random import randint
from brain_games.cli import a


def prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count != 3:
        question = randint(2, 50)
        print('Question: ' + str(question))
        x = 0
        for i in range(2, question // 2 + 1):
            if question % i == 0:
                x = x + 1
        if (x <= 0):
            correct = 'yes'
        else:
            correct = 'no'
        answer = prompt.string('Your answer: ')
        if answer == correct:
            print('Correct!')
            count += 1
        else:
            return(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct}'.\n Let's try again, {a}!")
            break
        if count == 3:
            return("Congratulations, " + a + "!")
