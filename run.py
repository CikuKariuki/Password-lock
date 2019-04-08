#!/usr/bin/env python3.6
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

def display_credentials(Credentials):
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

