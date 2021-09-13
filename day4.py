# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# sentence = input('Type in something: ')


def caps_counter(sent):
    upper_count = 0
    lower_count = 0
    for i in sent:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    print(f'UPPERCASE: {upper_count}\nLOWERCASE: {lower_count}')


# caps_counter(sentence)


# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a
num = int(input('Enter your number: '))
string = 'a+aa+aaa+aaaa'
values = string.split('+')
total = 0
for i, val in enumerate(values):
    values[i] = val.replace('a', '9')
for i in values:
    total += int(i)

print(total)
