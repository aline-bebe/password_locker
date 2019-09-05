import unittest
from login import Locker 


class TestLocker(unittest.TestCase):
    '''
    Test class that defines test cases for the login class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_lock = Locker("alexie","rusarwa","4444","alexie@ms.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_lock.first_name,"alexie")
        self.assertEqual(self.new_lock.last_name,"rusarwa")
        self.assertEqual(self.new_lock.password,"4444")
        self.assertEqual(self.new_lock.email,"alexie@ms.com")

    def test_save_data(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the lock list
        '''
        self.new_lock.save_data() # saving the new data
        self.assertEqual(len(Locker.locker_list),1)


if __name__ == '__main__':
    unittest.main()
      