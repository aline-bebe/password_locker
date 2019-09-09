import unittest
import pyperclip
from credentials import Credential

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Credential("gigi","4444","facebook","bebe@c.com") 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

       
        self.assertEqual(self.new_cred.username,"gigi")
        self.assertEqual(self.new_cred.password,"4444")
        self.assertEqual(self.new_cred.new_account,"facebook") 
        self.assertEqual(self.new_cred.email,"bebe@c.com")  

    def test_save(self):
        '''
        test_save_data test case to test if the  object is saved into
         the cred... list
        '''
        self.new_cred.keeped() # saving the new data
        instagram=Credential('aline','aline','instagram','aline@hhh')
        instagram.keeped()
        self.assertEqual(len(Credential.list_cred),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.list_cred= []

    def test_save_multiple(self):
        '''
        test_save_multiple_data to check if we can save multiple credentials
        objects to our cred_list
        '''
        self.new_cred.keeped()
        test_cred = Credential("ally","3333","wastap","bebe@c.com") # new data
        test_cred.keeped()
        self.assertEqual(len(Credential.list_cred),2)
    def test_display(self):
        '''
        display users
        '''
        self.assertEqual(Locker.display(),Locker.locker_list)
    def test_diplay_cred(self):
        '''
        method to display credentials
        '''

        self.new_cred.keeped()
        instagram=Credential("aline","aline","instragram","aline")
        instagram.keeped()
        self.assertEqual(len(Credential.excute(instagram.username)),1)

    def test_delete(self):
        '''
        test_delete to test if we can remove a data from our cred list
        '''
        self.new_cred.keeped()
        test_cred = Credential("ally","3333","wastap","bebe@c.com") # new data
        test_cred.keeped()

        self.new_cred.remove()# Deleting a data object
        self.assertEqual(len(Credential.list_cred),1)

    def test_find(self):
        '''
        test to check if we can find a data by using name and display information
        '''

        self.new_cred.keeped()
        test_cred = Credential("ally","3333","wastap","bebe@c.com") # new contact
        test_cred.keeped()

        find_name = Credential.find_username("ally")

        self.assertEqual(find_name.new_account,test_cred.new_account)

    def test_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the our object.
        '''

        self.new_cred.keeped()
        test_cred = Credential("gigi","4444","facebook","bebe@c.com") 
        test_cred.keeped()

        existing = Credential.cred_exists("gigi")

        self.assertTrue(existing)


    def test_display(self):
        '''
        method that returns a list of all objects saved
        '''
        self.new_cred.keeped()
        instagram=Credential("bebe","3333","twitter","bebe@c.com")
        instagram.keeped()

        self.assertEqual(len(Credential.excute(instagram.username)),1)

    def copy_name(self):
        '''
        Test to confirm that we are copying the name address from our data
        '''

        self.new_cred.keeped()
        Credential.copy_username("gigi")

        self.assertEqual(self.new_cred.username,pyperclip.paste())






if __name__ == '__main__':
    unittest.main()
