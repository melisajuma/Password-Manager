class User:>
    '''
    The User class will contain user details
    '''

    def __init__(self, login, password):
        '''
        This will ensure the user class has unique properties
        '''
        self.login = login
        self.password = password

    def user_exist(self, password):
        '''
        This will first verify that the user exists before showing the passwords
        Args:
            the user password
        return:
            boolean
        '''
        if self.password == password:
            return True
        else:
            return False
