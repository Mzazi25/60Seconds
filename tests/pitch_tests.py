import unittest
from  app .models import Pitch

class PostLikeModelTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Pitch Model
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_user = Pitch(Pitch= 'Mzazicaleb')
    def test_Pitch(self):
        self.assertTrue(self.test_Pitch is not None)