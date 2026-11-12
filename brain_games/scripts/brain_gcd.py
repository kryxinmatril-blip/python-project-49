import random

import prompt


def main():
    sum = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    while sum < 3:
        a = round(random.uniform(0, 100))
        b = round(random.uniform(0, 100))
        print(f'Question: {a} {b}')
        answer = prompt.string('Your answer: ')

        if b == 0:
            corect_answer = a
        else:
            while b != 0:
                a, b = b, a % b
            corect_answer = a

        if answer == str(corect_answer):
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
