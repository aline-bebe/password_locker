class Locker:
    """
    Class that generates new instances of password 
    """
    locker_list = [] # Empty users list

    def __init__(self,first_name,last_name,password,email):

        '''
        __init__ method that helps us define properties for our objects.

       
        '''
        self.first_name = first_name
        self.last_name =  last_name
        self.password = password
        self.email =  email 

    def save_data(self):

        '''
        save_data method saves locker objects into locker_list
        '''

        Locker.locker_list.append(self)

    def delete_data(self):

        '''
        delete_data method deletes a saved data from the locker_list
        '''

        Locker.locker_list.remove(self)
    # pass