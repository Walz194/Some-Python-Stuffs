# Question 18

import re


def pword_validity(password):
    upper_case = False
    lower_case = False
    number = False
    special_char = False
    min_length = False

    password_re = re.compile(r'^[a-zA-z0-9$#@]{6,12}$')
    pattern = password_re.match(password)
    try:
        groupie = pattern.group()
        for i in groupie:
            if i.islower:
                lower_case = True
            if i.isupper:
                upper_case = True
            if i.isdigit:
                number = True
            if i in ('$', '#', '@'):
                special_char = True
            min_length = True
        if upper_case == True and lower_case == True and number == True and special_char == True and min_length == True:
            print(f'{password} is VALID password!')
        else:
            print(f'{password} is NOT A VALID password')

    except AttributeError:
        print('Not a valid password')


user_pword = input('Enter your passwords seperated by commas:__').split(', ')

for pword in user_pword:
    pword_validity(pword)

wal
