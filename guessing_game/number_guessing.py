import random
from translate import Translator
import csv

translator = Translator(to_lang='en')


# This function is meant to allow the users to choose multiple languages
def choose_language():
    global translator
    print("Choose a language to work with. If none is chosen english will be used \n\t1) English\n\t2) Japanese\n\t3) Korean\n\t4) Portuguese\n\t5) Chinese ")
    ans = int(input("-:"))

    if ans == 1:
        translator.to_lang = 'en'
    elif ans == 2:
        translator = Translator(to_lang='ja')
    elif ans == 3:
        translator = Translator(to_lang='ko')
    elif ans == 4:
        translator = Translator(to_lang='pt')
    elif ans == 5:
        translator = Translator(to_lang='zh')


def guess(x, y):
    '''
        This is responsible for initiation the guessing game which users play
    '''
    comp_choice = random.randint(x, y)  # Computers generated value
    count = 1  # Variable to keep track of the number of guesses the user made. Initialy set to one
    try:
        choice = int(input(translator.translate(
            f'Guess a number between {x} and {y}: ')))
    except ValueError:
        # Anticipating the users to try and break us
        choice = int(input(translator.translate('Enter a valid integer: ')))

    while True:
        if choice == comp_choice:
            print(translator.translate(
                f'Correct! {choice} was the guessed number. Took you {count} tries'))
            break
        elif choice < comp_choice:
            print(translator.translate(
                'Sorry! Not what was guessed, mine is HIGHER'))
            choice = int(input(translator.translate('Try Again: ')))
            count += 1
            continue
        else:
            print(translator.translate('Sorry! Not what i guessed, mine is LOWER'))
            choice = int(input(translator.translate('Try Again: ')))
            count += 1
            continue

    print(translator.translate('GAME OVER!!!'))


# This creates a user object and adds the user to the data file
def create_user(name):
    user_obj = None
    if str.isdecimal(name):
        print(f'"{name}" is not a valid name')
        return user_obj
    else:
        # The object to be returned by the function
        user_obj = {'name': name, 'wins': 0}
        # File mode set to append, so as to add the new user to the file without overwriting it
        f = open('./data.csv', 'a', newline='')
        fieldnames = ['name', 'wins']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writerow(user_obj)
        f.close()
    return user_obj


def choosing_user():
    # Chooses the appropriate user, otherwise creates the user
    q1 = input(translator.translate('Are you an existing user?: '))

    # Trying to catch the possible inputs of the user
    yes = ['y', 'yes', 't', 'true', 'yeah']
    no = ['n', 'no', 'f', 'false', 'nope']

    if q1.lower() in yes:
        # Receiving the username of the user
        user_name = input(translator.translate('Enter your username: '))
        f = open('./data.csv', mode='r')
        csv_read = csv.DictReader(f)
        csv_list = list(csv_read)

        found = False

        for user in csv_list:
            if user['name'] == user_name:
                found = True
                print(translator.translate(
                    'Welcome {0}, been a while. You currently have {1} win{2}'.format(user["name"], user["wins"], 's' if int(user['wins']) > 1 else '')))
                return user
        if found == False:
            print(translator.translate(
                'Not an existing user, creating an account....'))
            return create_user(user_name)

    elif q1.lower() in no:
        user_name = input(translator.translate(
            'Enter your desired username: '))
        user = create_user(user_name)
        while user == None:
            user_name = input(translator.translate(
                'Can\'t enter integers as a user name, Try Again: '))
            user = create_user(user_name)
        return user
    else:
        print(translator.translate('Not a valid option'))
        choosing_user()


def play_game():
    # This starts the entire process
    choose_language()
    current_user = choosing_user()
    guess(1, 20)
    fieldnames = ["name", "wins"]
    f = open("./data.csv", mode='r')
    reader = csv.DictReader(f, fieldnames=fieldnames)
    temp_list = []  # temporary list to store new data

    for user in reader:
        if current_user["name"] == user["name"]:
            user['wins'] = int(user['wins']) + 1
            print(translator.translate(
                "Scores update: {1}, you have {0} win{2}".format(user["wins"], user["name"], 's' if user['wins'] > 1 else '')))
        temp_list.append(user)
    f.close()

    f = open('./data.csv', mode='w')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for item in temp_list:
        writer.writerow(item)
    f.close()


play_game()
