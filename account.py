class User:
    """
    Class that generates new instances of username
    """

    def __init__(self,username):
        """
        __init__method helps define properties of objects
       
       Arg:
            username: Name associated with account
        """
        self.username = username

class Credentials:
    """
    Class that generate new instances of passwords
    """

    def __init__(self,password):
        """
        init method that helps define password properties
        Arg:
            password:password for specific account
        """
        self.password = password
    account_list = []

    def save_credentials(self):
        """
        save_credentials method saves credential objects into account_list
        """
        Credentials.account_list.append(self)




