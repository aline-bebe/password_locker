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