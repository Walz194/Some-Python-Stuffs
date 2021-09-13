import random
# import pdb


# Data part of the program
user_data = [
    # {name, wins}
    {"name": "Olawale", "wins": 0}, {"name": "Bukky", "wins": 0}
]


def guess(x, y):
    '''
        This is responsible for initiation the guessing game which users play
    '''
    comp_choice = random.randint(x, y)  # Computers generated value
    count = 1  # Variable to keep track of the number of guesses the user made. Initialy set to one
    try:
        choice = int(input(f'Guess a number between {x} and {y}: '))
    except ValueError:
        # Anticipating the users to try and break us
        choice = int(input('Enter a valid integer: '))

    while True:
        if choice == comp_choice:
            print(
                f'Correct! {choice} was the guessed number. Took you {count} tries')
            break
        elif choice < comp_choice:
            print('Sorry! Not what was guessed, mine is HIGHER')
            choice = int(input('Try Again: '))
            count += 1
            continue
        else:
            print('Sorry! Not what i guessed, mine is LOWER')
            choice = int(input('Try Again: '))
            count += 1
            continue

    print('GAME OVER!!!')


def create_user(name):
    # This is responsible for creating a user. This enables me to use the DRY principle
    user_obj = {"name": name, "wins": 0}
    user_data.append(user_obj)
    return user_obj


def choosing_user():
    # Chooses the appropriate user, otherwise creates the user
    q1 = input('Are you an existing user?: ')

    # Trying to catch the possible inputs of the user
    yes = ['y', 'yes', 't', 'true', 'yeah']
    no = ['n', 'no', 'f', 'false', 'nope']

    if q1.lower() in yes:
        user_name = input('Enter your username: ')

        for user in user_data:
            if user["name"] == user_name:
                print(
                    f'Welcome {user["name"]}, been a while. You currently have {user["wins"]} wins')
                return user
            else:
                print('Not an existing user, creating an account....')
                return create_user(user_name)

    elif q1.lower() in no:
        user_name = input('Enter your desired username: ')
        return create_user(user_name)
    else:
        print('Not a valid option')
        q1 = input('Are you an existing user?: ')


def play_game():
    # This starts the entire process
    current_user = choosing_user()
    guess(1, 20)
    for user in user_data:
        if user["name"] == current_user["name"]:
            user["wins"] += 1
            print("Scores update: {1}, you have {0} wins".format(
                user["wins"], user["name"]))


play_game()
