import re
pattern = re.compile(r'^[A-za-z0-9$#@%]{8,}[0-9]$')
done = False

while done == False:
    string = input('Enter a password for testing: ')
    a = pattern.match(string)
    if a == None:
        string = input('Invalid Password, Try Again: ')
    else:
        print(a.group())
        ans = input('Do you want to try again? (y/n): ')
        if ans.lower() == 'y':
            continue
        else:
            done = True



