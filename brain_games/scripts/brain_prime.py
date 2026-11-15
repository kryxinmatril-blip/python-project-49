import random

import prompt


def main():
    def simple_number(number):
        if number == 1:
            return 'no'
        for i in range(2, number):
            if number % i == 0:
                return 'no'
        return 'yes'

    sum = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(Answer "yes" if given number is prime. Otherwise answer "no".)

    while sum < 3:
        ask = round(random.uniform(2, 100))
        print(f'Question: {ask}')
        answer = prompt.string('Your answer: ').strip().lower()
        if answer == simple_number(ask):
            print('Correct!')
            sum += 1
        else:
            print(f"""'no' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!""")
            break

    if sum == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
