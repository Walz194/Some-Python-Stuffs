# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number
import math


def gen_tup_list(*args):
    print(args, list(args))


# gen_tup_list(1, 2, 3, 4, 5, 6, 7)

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods


class PrintingString():
    def __init__(self, string):
        self._string = string

    def getString(self):
        return self._string

    def printString(self):
        print(self.getString())


# name = PrintingString('Olawale')
# name.printString()

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 C D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence


# sequence = input('Enter a string of number(s) seperated by comma: ')
# sequence_list = sequence.split(',')

def calculate(sequence):
    c = 50
    h = 30
    for num in sequence:
        q = math.floor(math.sqrt((2 * c * int(num)) / h))
        print(q, end=', ')


# calculate(sequence_list)

# Using list comprehension
def calc(d):
    c = 50
    h = 30
    q = math.sqrt((2 * c * d) / h)
    return q


# d = [i for i in input('Enter your numbers seperated by comma: ').split(',')]
# d = [int(i) for i in d]
# d = [round(calc(i)) for i in d]
# d = [str(i) for i in d]

# print(','.join(d))

# print(list(map(calc(), d)))

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i j

# x, y = map(int, input('Enter 2 numbers seperated by comma: ').split(','))
# tmp = []
# for a in range(x):
#     horizontal = []
#     for b in range(y):
#         horizontal.append(a*b)
#     tmp.append(horizontal)

# print(tmp)

# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

word_seq = input('Enter a sequence of words separated by comma: ').split(',')
word_seq.sort()
print(','.join(word_seq))
