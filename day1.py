# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line
def find_in_range(start, stop):
    for i in range(start, stop+1):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')


# find_in_range(2000, 3000)

# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

num_string = input("Enter you number(s) sparated by space: ")
num_list = num_string.split(" ")


def factorial():
    for num in num_list:
        fact = 1
        count = 1
        while count <= int(num):
            fact = fact * count
            count += 1
        print(f'{num}! = {fact}', end=", ")


# factorial()

# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def generate_dict(n):
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = i * i
    print(my_dict)


# generate_dict(20)
