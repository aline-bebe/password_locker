from login import Locker 
class Credential:
    """
    Class that generates new instances of credential 
    """
    list_cred = [] 
    list_credentials= []

    def __init__(self,username,password,new_account,email):

        '''
        __init__ method that helps us define properties for our objects.

       
        '''
       
        self.username =  username
        self.password = password
        self.new_account =  new_account
        self.email =  email

    # def save_cred(self):
    #     '''
    #     to save all credentials
    #     ''''
    #     Credential.
    def keeped(self):

        '''
        save_data method saves  objects into cred_list
        '''

        Credential.list_cred.append(self)

    def remove(self):

        '''
        delete_data method deletes a saved data from the cred_list
        '''

        Credential.list_cred.remove(self)


    @classmethod
    def find_username(cls,username):
        '''
        Method that takes in a name and returns a data that matches that name.

        Args:
            name: username to search for
        Returns :
            data of person that matches the name.
        '''

        for credentials in cls.list_cred:
            if credentials.username == username:
                return credentials



    @classmethod
    def cred_exists(cls,username):
        '''
        Method that checks if a objects exists from the  list.
        Args:
           name to search if it exists
        Returns :
            Boolean: True or false depending if the our object exists
        '''
        for credentials in cls.list_cred:
            if credentials.username == username:
                    return True

        return False

    @classmethod
    def excute(cls,username):
        '''
        method that returns the list
        '''
        list_credentials= []
        for credentials in cls.list_cred:
            if credentials.username == username:
                list_credentials.append(credentials)
                
       
        return list_credentials

    @classmethod
    def copy_username(cls,username):
        checking = Credential.find_username(username)
        pyperclip.copy(checking.username)

    @classmethod
    def checking(cls,email,password):
        login_user=''
        for login in Locker.locker_list:
            if(login.email== email and login.password==password):
                login_user=login.email
        return login_user
