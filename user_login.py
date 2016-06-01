import csv


def create_user():
    user_name = input('Choose a Username: ')
    user_password = input('Choose a Password: ')
    user_fullname = input('Enter full name: ')
    additional_info = input('*optional information: ')

    user_data = ('{}, {}, {}, {}').format(user_name, user_password, user_fullname, additional_info)
    print(user_data)
    # search databse for username

    with open('user_database.csv') as infile:
        database = infile.readlines()
    if user_name in database.csv:
        print('Sorry, username taken')
    else:
        with open('user_database.csv', 'a') as outfile:
            outfile.write(user_data)

    print('User {} succesfully created.'.format(user_name))


def login_user():
    username_attempt = input('Enter username: ')
    password_attempt = input('Enter password: ')

    with open('user_database.csv') as infile:
        attempts = 0
        database = csv.DictReader(infile, fieldnames=['user_name', 'user_password', 'user_fullname', 'additional_info'])
        while attempts < 5:
            for line in database:
                if line['user_name'] == username_attempt:
                    username = 1
                else:
                    username = 0
                if line['user_password'] == password_attempt:
                    password = 1
                else:
                    password = 0
                if username + password == 2:
                    print('Welcome {}.'.format(username_attempt))
                    view_data = 'v'
                    logout = 'l'
                    action = input('''What would you like to do?
                            (v) - View user data
                            (l) - Logout''').lower()
                    if action == view_data:
                        print('''User Fullname: {}
                                Additional information: {}'''.format(user_fullname, additonal_info))
                    elif action == logout:
                        pass
                        # logout
                else:
                    print('Sorry, login unsuccesful.')
                    attempts += 1
                    remaining_attempts = 5 - attempts
                    print('{} login attempts remaining.'.format(remaining_attempts))
        if attempts > 5:
            print('You are out of login attempts')

screen_answer = input('Would you like to (l)og in or (c)reate user? ')
if screen_answer == 'c':
    create_user()
if screen_answer == 'l':
    login_user()
