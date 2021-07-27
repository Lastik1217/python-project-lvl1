#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    imya = prompt.string('May I have your name? ')
    print('hello, {}!'.format(imya))
    return imya


name = welcome_user()
