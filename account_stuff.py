#Already existing user
existing_users = [{'username':'Olawale','password':'password'},{'username':'Afeez','password':'password'},{'username':'Mubarak','password':'password'},{'username':'Ahmed','password':'password'}]

question1 = input('Are you an existing user? [Y/N]: \n')

if question1 == 'Y' or 'y':
    name = input('Enter your username: ')
    username = []
    for user in existing_users:
        username.append(user['username'])
        
    if name in username:
        password = input('Alright, proceed to password: \n')
        for user in existing_users:
            if user['username'] == name and user['password'] == password:
                print('Welcome!!! You are logged in')
                break
            else:
                print('Incorrect Password')
        
    else:
        question2 = input('That is not a registered user, would you like an account? [Y/N]')
        
        if question2 == 'Y' or 'y':
            new_user = {'username': name, 'password': None}
            password = input('Enter a password: \n')
            new_user['password'] = password
            existing_users.append(new_user)
            print('All done!!! Have a good day Bro.')
        else:
            print('Good day!!! Thanks for wasting my time')
else:
    name = input("Enter a username to create an account: \n")
    password = input("Enter a password")
    new_user = {'username': name, 'password': password }
    existing_users.append(new_user)
    print("All done. Thanks for your time")
