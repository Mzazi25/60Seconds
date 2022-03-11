import unittest
from  app .models import User

class UserModelTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Users Model
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_user = User(password= 'Mzazicaleb')
    def test_password(self):
        self.assertTrue(self.new_user.password is not None)