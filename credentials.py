class Credential:
    """
    Class that generates new instances of credential 
    """
    list_cred = [] 

    def __init__(self,username,password,new_account):

        '''
        __init__ method that helps us define properties for our objects.

       
        '''
       
        self.username =  username
        self.password = password
        self.new_account =  new_account


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

