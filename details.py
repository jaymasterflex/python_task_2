import random
import string

new_employee = True
while new_employee:
    user_data = []

    first = input('\nEnter your first name: ')
    last = input('Enter your last name: ')
    email = input('Enter your email: ')

    user_data.append(first)
    user_data.append(last)
    user_data.append(email)


    def generate_password(first, last):
        set1 = first[0:2]
        set2 = last[-2:]
        return set1 + set2


    def randomStringDigits(generate_password, stringLength=5):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
    password = generate_password(first, last) + randomStringDigits(5)
    user_data.append(password)


    satisfied = input('Are you satisfied with password [' + password + '] enter "y" for YES or press any key to customize password: ').lower()
    if satisfied == 'y':
        print('\nFirst name: ', (user_data[0]))
        print('Last name: ', (user_data[1]))
        print('Email: ', (user_data[2]))
        print('Password: ', (user_data[3]))
    else:
        print('password must be at least 7 characters')
        def checkPassword(custom_password):
            """
            Validate the password
            """
            if len(custom_password) < 7:
                # Password too short
                print("Your password must be at least 7 characters.")
                return False
            else:
                # All good
                user_data.append(custom_password)
                print(' \nFirst name: ', (user_data[0]))
                print('Last name: ', (user_data[1]))
                print('Email: ', (user_data[2]))
                print('Password: ', (user_data[4]))
                return True            
        # Prompt user to enter valid password
        passwordValid = False
        while not passwordValid:
            custom_password = input("Type in your password: ")
            passwordValid = checkPassword(custom_password)

    print('\nInput another employee?')
    new_employee = input('Press any key to enter new employee or "n" for NO: ').lower()
    if new_employee == 'n':
        break
