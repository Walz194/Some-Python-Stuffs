num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
total = num1 + num2

ans = input('Do you want to enter another number? [Y/N]')

while ans.lower() == 'y':
    total += int(input("Enter another number: "))
    ans = input('Do you want to enter another number? [Y/N]')

print(f'The total is {total}')
