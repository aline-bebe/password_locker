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

    @classmethod
    def find_email(cls,email):
        '''
        Method that takes in a email and returns a data that matches that number.

        Args:
            email: email to search for
        Returns :
            data of person that matches the email.
        '''

        for login in cls.locker_list:
            if login.email == email:
                return login


    @classmethod
    def data_exists(cls,email):
        '''
        Method that checks if a objects exists from the locker list.
        Args:
            email: email to search if it exists
        Returns :
            Boolean: True or false depending if the our object exists
        '''
        for login in cls.locker_list:
            if login.email == email:
                    return True

        return False

    @classmethod
    def display(cls):
        '''
        method that returns the locker list
        '''
        return cls.locker_list

    @classmethod
    def copied_email(cls,email):
        check = Contact.find_email(email)
        pyperclip.copy(check.email)

    # pass