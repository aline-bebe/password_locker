import unittest
from login import Locker 
import pyperclip


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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Locker.locker_list = []

    def test_save_multiple_data(self):
        '''
        test_save_multiple_data to check if we can save multiple locker
        objects to our locker_list
        '''
        self.new_lock.save_data()
        test_user = Locker("bebe","ally","3333","bebe@gmail.com") # new data
        test_user.save_data()
        self.assertEqual(len(Locker.locker_list),2)

    def test_delete_data(self):
        '''
        test_delete_data to test if we can remove a data from our locker list
        '''
        self.new_lock.save_data()
        test_user = Locker("bebe","ally","3333","bebe@gmail.com") # new data
        test_user.save_data()

        self.new_lock.delete_data()# Deleting a data object
        self.assertEqual(len(Locker.locker_list),1)

    def test_find_data_by_email(self):
        '''
        test to check if we can find a data by using email and display information
        '''

        self.new_lock.save_data()
        test_user = Locker("bebe","ally","3333","bebe@gmail.com") # new contact
        test_user.save_data()

        find_email = Locker.find_email("bebe@gmail.com")

        self.assertEqual(find_email.email,test_user.email)

    def test_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the our object.
        '''

        self.new_lock.save_data()
        test_locker = Locker("alexie","rusarwa","4444","alexie@ms.com") 
        test_locker.save_data()

        data_check = Locker.data_exists("alexie@ms.com")

        self.assertTrue(data_check)

    def test_to_display(self):
        '''
        method that returns a list of all objects saved
        '''

        self.assertEqual(Locker.display(),Locker.locker_list)

       


    def copy_name(self):
        '''
        Test to confirm that we are copying the name address from our data
        '''

        self.new_lock.save_data()
        Locker.copied_name("alexie@ms.com")

        self.assertEqual(self.new_lock.email,pyperclip.paste())

          


if __name__ == '__main__':
    unittest.main()
      