#!/usr/bin/env python3.6
import random
from account import Credentials 
from account import User

def create_account(users_name,username,password):
    """
    function to create new credentials for a new account
    """
    new_account = User(users_name)
    new_account = Credentials(username,password)
    return new_account

def save_credentials(credentials):
    """
    function that saves the user's credentials
    """
    credentials.save_credentials()

def del_credentials(credentials):
    """
    function that deletes credentials
    """
    credentials.del_contact()

def find_credentials(username):
    """
    function that finds credentials by username and returns all credentias
    """
    return Credentials.find_by_username(username)

def display_credentials():
    """
    function that returns all saved credentials
    """
    return Credentials.display_credentials()

def copy_credentials(Credentials):
    """
    function that return copied credentials, those in clipboard
    """
    return Credentials.copy_credentials()

def main():
    print("Hello, create a new account. What is your name?")
    username = (input())

    print(f"Hey {username}, what account would you like to create?")
    print('\n')
    while True:
        print("Use these short codes: ca-create a new account, dc-display credentials, fc-find credentials, ex-exist account_list ")
        short_code = input().lower()

        if short_code == 'ca':
            print("New Account")
            print("-"*10)

            print("User's_name")
            users_name = input()

            print("username")
            username = input()

            print("would you want a generated password? y/N")
            answer = input()
            if answer == 'y':
                chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789~!@#$%^&**()_+=+'
                length= int(input('password length?'))
                password=''
                for i in range(length):
                    password = random.choice(chars)
                print("password")
            else: 
                print("password")
                password=input()    

            save_credentials(create_account(users_name,username,password))
            print('\n')
                
        elif short_code == 'dc':
            if display_credentials():
                print("here is a list of account usernames and passwords")
                print('\n')
                for credentials in display_credentials():
                    print(f"{credentials.username}{credentials.password}")
                    print('\n')
            else: print('\n')
            print("You don't seem to have any accounts yet")
            print('\n')

        elif short_code == 'fc':
            print("Enter the username you want to search for")
            search_username = input()
            if find_credentials(search_username):
                search_credentials = find_credentials(search_username)
                print(f"Username {search_credentials.username}")
                print(f"Password {search_credentials.password}")
            else: print("that username does not exist")

        elif short_code == 'ex':
            print(f"Bye {username}")
            break
        else: print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
    