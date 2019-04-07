class User:
    """
    Class that generates new instances of user's_name
    """

    def __init__(self,users_name):
        """
        __init__method helps define properties of objects
       
       Arg:
            users_name: Name associated with account
        """
        self.users_name = users_name

class Credentials:
    """
    Class that generate new instances of passwords
    """

    def __init__(self,username,password):
        """
        init method that helps define password properties
        Arg:
            password:password for specific account
        """
        self.username = username
        self.password = password
    account_list = []

    def save_credentials(self):
        """
        save_credentials method saves credential objects into account_list
        """
        Credentials.account_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method deletes credential object from account_list
        """
        Credentials.account_list.remove(self)

    @classmethod #decorator(informs python that this is a method for the entire class)
    def find_by_username(cls,username):
        """
        method that takes in a username and returns credentials that match that username
        """
        for credentials in cls.account_list:
            if credentials.username == username:
                return credentials


