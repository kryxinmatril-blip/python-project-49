import prompt
import random

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ask = round(random.uniform(1, 100))
    print(f'Question: {ask}')
    answer = prompt.string('Your answer: ')
    if ask % 2 == 0:
        if answer == 'yes':
            print('Correct!')
        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.")    
    
    if ask % 2 != 0:
        if answer == 'no': 
            print('Correct!')
        else:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.")

if __name__ == "__main__":
    main()

