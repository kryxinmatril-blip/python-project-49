import random

import prompt


def main():
    coll = []
    step_progressoin = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
