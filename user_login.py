import csv


def create_user():
    user_name = input('Choose a Username: ').lower()
    user_password = input('Choose a Password: ').lower()
    user_fullname = input('Enter full name: ').lower()
    additional_info = input('*optional information: ').lower()

    user_data = ('{},{},{},{}\n').format(user_name, user_password, user_fullname, additional_info)

    with open('user_database.csv') as infile:
        database = infile.readlines()
    for line in database:
        if user_name in line:
            print('Sorry, username taken')
        else:
            with open('user_database.csv', 'a') as outfile:
                outfile.write(user_data)
                print('User {} succesfully created.'.format(user_name))


def login_user():
    # Does NOT work yet

    with open('user_database.csv') as infile:
        attempts = 0
        database = csv.DictReader(infile, fieldnames=['user_name', 'user_password', 'user_fullname', 'additional_info'])
        while attempts < 6:
            remaining_attempts = 5 - attempts
            print('enter "exit" to leave')
            username_attempt = input('Enter username: ').lower()
            password_attempt = input('Enter password: ').lower()
            if attempts == 5:
                print('You are out of login attempts')
            if username_attempt == "exit" or password_attempt == 'exit':
                    break
            for line in database:
                if line['user_name'] == username_attempt and line['user_password'] == password_attempt:
                    print('Correct')
                    print('Welcome {}.'.format(username_attempt))
                    view_data = 'v'
                    logout = 'l'
                    action = input('''What would you like to do?
                            (v) - View user data
                            (l) - Logout\n''').lower()
                    if action == view_data:
                        while True:
                            print('Enter "e" to exit')
                            user_fullname = line['user_fullname']
                            additional_info = line['additional_info']
                            print('''User Fullname: {}
Additional information: {}'''.format(user_fullname, additional_info))
                            prompt = input('')
                            if prompt == 'e':
                                break
                    if action == create_user:
                        create_user()
                    elif action == logout:
                        return

                elif line['user_name'] == username_attempt:
                    if line['user_password'] != password_attempt:
                        continue
            else:
                print('Sorry, login unsuccesful.')
                attempts += 1
                print('{} login attempts remaining.'.format(remaining_attempts))

while True:
    print('Enter "exit" to leave')
    screen_answer = input('Would you like to (l)og in or (c)reate user? ')
    if screen_answer == 'c':
        create_user()
    elif screen_answer == 'l':
        login_user()
    elif screen_answer == 'exit':
        break
