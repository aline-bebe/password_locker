#!/usr/bin/env python3.6
import pyperclip


from login import Locker
from credentials import Credential
def display():
    '''
    function to display users
    '''
    return Locker.display()
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

def create_cred(username,app_name,password,email):
    '''
    Function to create new credentials
    '''
    new_cred=Credential(username,app_name,password,email)
    return new_cred

def keeped(credentials):
    '''
    Function to save credentials
    '''
    credentials.keeped()

def excute(username):
    '''
    Function to display credentials
    '''
    return Credential.excute(username)

def copy_cred(app_name):
    '''
    Function to copy credentials
    '''
    return Credential.copy_cred(app_name)
# def save_cred(credentials):
#     '''
#     save all credentials
#     '''
#     Credential.save_cred(credentials)

def main():
    print(' ')
    print("Hello Welcome to your pass locker")
    while True:
        print(' ')
        print("-"*100)
        print("Use these short codes :\n cc - create a new account \n dc- dispaly users \n lg -login \n dl -delete account \n ex -exit ")
        short_code = input('enter a choice: ').lower().strip()

        if short_code == 'ex':
            break
        elif short_code == 'dl':
            print("-"*60)
            print(' ')
            print('already deleted')
            break
        elif short_code == 'dc':
            print("-"*60)
            print(' ')
            if display():
                print("name of all user:")
                for locker in display():
                    print(f'{locker.first_name}{locker.last_name} {locker.password} {locker.email}')
            else:
                print("you don't have any users")

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
            print(f'new account : {first_name}{last_name}{email} enter passwors: {password}')
            
        elif short_code == 'lg':
            print("-"*50)
            print(' ')
            print(' please login and enter your info:')
            email = input('enter your email - ').strip()
            password= str(input('enter your key - '))
            check = checking (email,password)
            if check == email:
                print(" ")
                print(f'welcome {email}.please choose onother option.')
                print(' ')
                while True:
                    print("-"*60)
                    print('to navigate to cred account use code:\n cc-create account \n dl- delete \n ex -exit')
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
                        # password = input('enter the password').strip()

                        while True:
                            print(' ')
                            print(" "*10)
                            print("choosing for credential: \n ky- enterpssword  \n gr generate pss \n ex exit")
                            key = input('enter a option: ').lower().strip()
                            print("-"*80)
                            if key == 'ky':
                                print(" ")
                                password = input('enter your password: ').strip()
                                break


                            # elif short_code == 'dl':
                            #     print("-"*80)
                            #     print(' ')
                            #     print('already deleted')
                            #     break

                            elif key == 'gr':
                                password = generate_pass()
                                break
                            elif key == 'ex':
                                break

                            else:
                                print('repeat it again.')
                        keeped(create_cred(username,app_name,password,email))
                        print(' ')
                        print(f'Credential Created: username: {username} -app_name:{app_name} -password:{password}')
                        print(' ')

                    elif short_code == 'ds':
                        print(' ')
                        if excute(username):
                            print('here is a list of all credentials')
                            print(' ')
                            for credentials in excute(username):
                                print(f'username: {username} -app_name: {app_name} -password: {password}')
                                print(' ')

                        else:
                            print(' ')
                            print("you don't have cred")
                            print(' ')

                # elif short_code == 'cp':
                #     print(' ')
                #     choise = input("enter the name of credentials app to copy: ")

                #     copy_cred(choise)
                #     print(' ')
                    
                else:
                    print(' ')
                    print('try again or create another one.')
            else:
                print("-"*80)
                print(' ')
                print("try again")
        else: 
            print('bye bye')


if __name__ == '__main__':
    main()



        

            
          
            

            




    





