# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

listy = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# odd = [(x**2 if x % 2 != 0 else x) for x in listy if x % 2 != 0]
odd = [str(int(i) ** 2) for i in listy if int(i) % 2]

# print(odd)

# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200
# D means deposit while W means withdrawal
map
print('Enter the operations you want')
count = 0
values = []
while True:
    try:
        entry = input('_')
        op = entry[0]
        num = int(entry[2:])
    except IndexError:
        break
    if op.lower() == 'd':
        values.append(num)
        count += 1
    elif op.lower() == 'w':
        values.append(num * -1)
        count += 1
    else:
        break

print(sum(values))
