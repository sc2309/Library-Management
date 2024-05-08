import datetime
import pandas as pd


def login(name, og_password):
    csv_file = 'data.csv'
    df = pd.read_csv(csv_file)
    result = df[df['name'] == name]

    if not result.empty:
        password2 = result['password'].values[0]
        if password2 == og_password:
            print('Login successful')  # next step from next file
        else:
            print('Login failed')                                              
    else:
        print(f"No record found for {name}.")


if __name__ == '__main__':
    current_time = datetime.datetime.now()

    formatted_time = current_time.strftime("%H:%M:%S")
    print(f'Time: {formatted_time}')
    opr = input('Hello User please select\nLogin / Sign in: ').lower()
    if opr == 'login':
        print(f'If you want to {opr} please enter the following details\n')
        name = input('Please enter your name: ').lower()
        password = input('Please enter your password: ')
        login(name,password)
    elif opr == 'sign in':
        print(f'If you want to {opr} please enter the following details\n')
        name = input('Please enter yoour name: ').lower()
        age = int(input('Please enter your age: '))
        phone = input('Please enter your phone number: ')
        password = input('Please enter a password(you will need it next time you login): ')
        re_pass = input('Please re-enter your password: ')
        if len(password) < 7:
            print('ERROR: Password cannot be lower than 7 digits')
        elif password != re_pass:
            print('ERROR: the re-entered password and original password dont match')
        else:
            data = [{'name': name, 'age': age, 'phone': phone, 'password': password}]
            new_df = pd.DataFrame(data)
            csv_file = 'data.csv'
            new_df.to_csv(csv_file, mode='a', header=False, index=False)
            print('Sign in successfull, now please proceed for login')

    else:
        print('ERROR: Incorrect operation')

