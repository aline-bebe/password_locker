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