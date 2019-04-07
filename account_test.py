import unittest
from account import User #importing the user class
from account import Credentials #importing the credentials class

class TestUser(unittest.TestCase): #testcase checks for an expected result
    """
    Test class that defines test cases for the behaviours of the user and credentials classes.

    Arg:
        unittest.TestCase: TestCase class is used to help in creating test cases
    """

    def setUp(self):
        """
        The setup method is used to run before each testcase.
        """
        self.new_account = User("James") #create user object
    
    def test_init(self):
        """
        test_init test case to test if the object was initialised properly
        """

        self.assertEqual(self.new_account.users_name,"James")

class TestCredentials(unittest.TestCase): #testcase checks for an expected result
    """
    Test class that defines test cases for the behaviours of the user and credentials classes.

    Arg:
        unittest.TestCase: TestCase class is used to help in creating test cases
    """

    def setUp(self):
        """
        The setup method is used to run before each testcase.
        """
        self.new_account = Credentials("TwitterJames","12345678") #create credentials object
    
    def test_init(self):
        """
        test_init test case to test if the object was initialised properly
        """
        self.assertEqual(self.new_account.username,"TwitterJames")
        self.assertEqual(self.new_account.password,"12345678")
    
    def test_save_credentials(self):
        """
        test_save_user test case to test if user object is saved 
        """
        self.new_account.save_credentials() #save the user info
        self.assertEqual(len(Credentials.account_list),1)

    def tearDown(self):
        """
        tearDown method does clean up after each test case has run
        """
        Credentials.account_list = []
        

    def test_save_multiple_credentials(self):
        """test to check if we can save multiple account credentials.
        """
        self.new_account.save_credentials()
        test_credentials = Credentials("InstaJames","Hello000")#new account
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.account_list),2)



if __name__ == '__main__':
    unittest.main()    