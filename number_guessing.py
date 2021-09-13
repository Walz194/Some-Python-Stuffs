import sys
import random

start = None
stop = None
if len(sys.argv) == 3:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])
    if start > stop:
        temp = start
        start = stop
        stop = temp


def guess(x=1, y=10):
    comp_choice = random.randint(x, y)
    count = 1
    try:
        choice = int(input(f'Guess a number between {x} and {y}: '))
    except ValueError:
        choice = int(input('Enter a valid integer: '))

    while True:
        if choice == comp_choice:
            print(
                f'Correct! {choice} was the guessed number. Took you {count} tries')
            break
        elif choice < comp_choice:
            print('Sorry! Not what was guessed, mine is HIGHER')
            choice = int(input('Try Again: '))
            count += 1
            continue
        else:
            print('Sorry! Not what i guessed, mine is LOWER')
            choice = int(input('Try Again: '))
            count += 1
            continue

    print('GAME OVER!!!')


try:
    guess(start, stop)
except TypeError:
    guess()
