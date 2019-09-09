#!/usr/bin/env python3.6
import pyperclip


from login import Locker
from credentials import Credential
def create_users(fname,lname,password,email):
    '''
    Function to create a new user
    '''
    new_lock = Locker(fname,lname,password,email)
    return new_lock

def save_data(login):
    '''
    Function to save data
    '''
    login.save_data()

def checking(email,password):
    '''
    Function to verfy the existance of user
    ''' 
    check = Credential.checking(email,password)
    return check

def generate_pass():
    '''
    Function to generate password
    '''
    key = Credential.generate_pass()
    return key

def create_cred(username,app_name,password):
    '''
    Function to create new credentials
    '''
    new_cred=Credential(username,app_name,password)
    return new_cred

def save_cred(credentials):
    '''
    Function to save credentials
    '''
    credentials.keeped()

def display_cred(username):
    '''
    Function to display credentials
    '''
    return Credential.display_cred(username)

def copy_cred(app_name):
    '''
    Function to copy credentials
    '''
    return Credential.copy_cred(app_name)

def main():
    print(' ')
    print("Hello Welcome to your pass locker")
    while True:
        print(' ')
        print("-"*100)
        print("Use these short codes :\n cc - create a new account \n lg -login \n dl -delete account \n ex -exit ")
        short_code = input('enter a choice: ').lower().strip()

        if short_code == 'ex':
            break
        elif short_code == 'dl':
            print("-"*60)
            print(' ')
            print('already deleted')
            break

        elif short_code == 'cc':
            print("-"*40)
            print(' ')
            print('creating new account:')
            first_name = input('enter your first_name - ').strip()
            last_name = input('enter last_name - ').strip()
            email = input('enter email - ').strip()
            password= input('enter your password - ').strip()
            save_data(create_users(first_name,last_name,email,password))
            print(" ")
            print(f'new account created for: {first_name}{last_name}{email} enter passwors: {password}')
            
        elif short_code == 'lg':
            print("-"*50)
            print(' ')
            print('login and please enter your details:')
            email = input('enter your email - ').strip()
            password= str(input('enter your key - '))
            check = checking (email,password)
            if check == email:
                print(" ")
                print(f'welcome {email}.please choose any option to continue.')
                print(' ')
                while True:
                    print("-"*60)
                    print('to navigate to cred account use code:\n cc-create account \n dc- display credentials \n dl- delete \n ex -exit')
                    short_code=input('enter a choice: ').lower().strip()
                    print("-"*90)
                    if short_code =='ex':
                        print(' ')
                        print(f'thank you! {email}.')
                        break
                    elif short_code == 'dl':
                        
                        print("-"*80)
                        print(' ')
                        print('deleted')
                        break

                    elif short_code == 'cc':
                        print(' ')
                        print('enter your new credential: ')
                        username = input('enter the user name-').strip()
                        app_name = input('enter the app name-').strip()
                        


                while True:
                    print(' ')
                    print(" "*80)
                    print("choosing for credential: \n ky- enterpssword \n dl- delete \n gr generate pss \n ex exit")
                    key = input('enter a option: ').lower().strip()
                    print("-"*80)
                    if key == 'ky':
                        print(" ")
                        password = input('enter your password: ').strip()
                        break


                    elif short_code == 'dl':
                        print("-"*80)
                        print(' ')
                        print('already deleted')
                        break

                    elif key == 'gr':
                        password = generate_pass()
                        break
                    elif key == 'ex':
                        break

                    else:
                        print('repeat it again.')
                save_cred(create_users(username,app_name,password))
                print(' ')
                print(f'Credential Created: username: {username} -app_name:{app_name} -password:{password}')
                print(' ')

        elif short_code == 'ds':
                print(' ')
                if display_cred(username):
                    print('here is a list of all credentials')
                    print(' ')
                    for credentials in display_cred(username):
                        print(f'username: {credentials.username} -app_name: {credentials.app_name} -password: {credentials.password}')
                        print(' ')

                else:
                    print(' ')
                    print("you don't have cred")
                    print(' ')

        elif short_code == 'cp':
            print(' ')
            choise = input("enter the name of credentials app to copy: ")

            copy_cred(choise)
            print(' ')
            
        else:
            print(' ')
            print('try again or create another one.')
    else:
            print("-"*80)
            print(' ')
            print("try again")


if __name__ == '__main__':
    main()



        

            
          
            

            




    





