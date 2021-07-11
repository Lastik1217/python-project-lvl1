#!/usr/bin/env python
import random
import operator
from brain_games.cli import a


def calc():
    print('What is the result of the expression?')
    operation_sign = \
        {'+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         }
    count = 0
    while count != 3:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        actions = list(operation_sign.keys())
        chosen = random.choice(actions)
        result = operation_sign[chosen](number_1, number_2)
        print(f'Question: {number_1} {chosen} {number_2}')
        answer = input('Your answer: ')

        if str(result) == answer:
            count += 1
            print('Correct!')
        else:
            return(f"'{answer}' is wrong answer ;(. "
                 f"Correct answer was '{result}'.\nLet's try again, {a}!")
            break
        if count == 3:
            return('Congratulations,' + a + '!')
