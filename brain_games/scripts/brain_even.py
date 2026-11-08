import random

import prompt


def main():
    sum = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while sum < 3:
        ask = round(random.uniform(1, 100))
        print(f'Question: {ask}')
        answer = prompt.string('Your answer: ').strip()
        if ask % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                sum += 1
            else:
                print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
                break

        if ask % 2 != 0:
            if answer == 'no':
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

