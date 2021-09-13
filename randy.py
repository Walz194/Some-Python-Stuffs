import random
comp_choice = random.randint(1, 10)

correct = False
your_choice = int(input('Enter a number btw 1 and 10: '))
while True:
    if your_choice == comp_choice:
        print(f'Wow, you\'re correct, {comp_choice} is the right answer')
        break
    else:
        if your_choice < comp_choice:
            your_choice = int(input(
                f'Your ans {your_choice} is lower than my choice. \nTry Again!: '))
        else:
            your_choice = int(input(
                f'Your ans {your_choice} is higher than my choice. \nTry Again!: '))
