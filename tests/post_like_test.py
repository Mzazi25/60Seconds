import unittest
from  app .models import PostLike

class PostLikeModelTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the PostLike Model
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_user = PostLike(PostLike= 'Mzazicaleb')
    def test_PostLike(self):
        self.assertTrue(self.test_PostLike is not None)