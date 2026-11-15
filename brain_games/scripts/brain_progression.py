import random

import prompt


def main():
    def progressions():
        start = random.randint(1, 10)
        step = random.randint(1, 10)
        hide_pos = random.randint(1, 10)
        true_answer = 0
        coll = []

        for i in range(10):
            if i == hide_pos - 1:
                coll.append('..')
                true_answer = i
            else:
                coll.append(start + step * i)

        return ' '.join(map(str, coll)), coll[true_answer - 1] + step

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    sum = 0

    while sum < 3:
        progression, corect_answer = progressions()
        print(f'Question: {progression}')
        answer = prompt.string('Your answer: ')

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
