# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

word = input('Enter a statement: ')

word = word.split(' ')

word = list(set(word))

word.sort()
# for i in word:
#     print(i)

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.


# def check(x):
#     return int(x, 2) % 5 == 0


# list = input('Enter some sequence: ').split(',')
# ans = filter(check, list)

# print(','.join(ans))

# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

lst = []
for i in range(1000, 3001):
    even_flag = 1
    for j in str(i):
        if ord(j) % 2 != 0:
            even_flag = 0
    if even_flag == 1:
        lst.append(str(i))

# print(','.join(lst))

# Write a program that accepts a sentence and calculate the number of letters and digits


def check(sent):
    letters = 0
    digit = 0
    for i in sent:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            digit += 1
    print(f'There are {letters} letters and {digit} digits in your sentence')


wale = input('Enter your sentence: ')
check(wale)
