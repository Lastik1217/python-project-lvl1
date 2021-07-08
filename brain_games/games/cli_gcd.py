#!/usr/bin/env python
import prompt
from random import randint
from brain_games.cli import a


def gcd():
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count != 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print('Question: ' + str(num1) + ' ' + str(num2))
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1
        nod = num1 + num2
        answer = prompt.integer('Your answer: ')
        if answer == nod:
            count += 1
            print('Correct!')
        else:
            return(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{nod}'.\n Let's try again, {a}!")
            break
        if count == 3:
            return("Congratulations, " + a + "!")