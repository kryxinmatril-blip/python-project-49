import random

import prompt


def main():
    sum = 0
    calc = '+-*'

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    while sum < 3:
        number1 = round(random.uniform(0, 100))
        number2 = round(random.uniform(0, 100))
        rand_operation = round(random.uniform(0, 2))
        print(f'Question: {number1} {calc[rand_operation]} {number2}')
        answer = prompt.string('Your answer: ')
        corect_answer = str(eval(f'{number1} {calc[rand_operation]} {number2}'))

        if answer == corect_answer:
            print('Correct!')
            sum += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{corect_answer}'.
Let's try again, {name}!""")
            break

    if sum == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
