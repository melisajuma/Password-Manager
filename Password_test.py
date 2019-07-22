import unittest  # importing unittest module
from Password_Locker import Password  # importing password class


class TestPassword(unittest.TestCase):
    """
    Here is where we will perfome all our test
    """

    def setUp(self):
        """
        This function will create a new instance password before each test
        """
        self.new_password = Password("twitter", "Melisa", "2030")

    def tearDown(self):
        """
        Here will be clearing password after every test to avoid confusion
        """
        Password.password = []

    def test_new_pass(self):
        """
        Here will test if a new password is initiated correctly
        """
        self.assertEqual(self.new_password.account, "twitter")
        self.assertEqual(self.new_password.username, "Melisa")
        self.assertEqual(self.new_password.password, "2030")

    def test_save_new_password(self):
        """
        Here it will check weather the new password is added in the list
        """
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list), 1)

    def test_add_generate_password(self):>
        """
        This will check if the new password added to the list
        """
        new_password = Password("facebook", "2017", Password.generate_(6))
        new_password.save_password()
        self.assertEqual(len(Password.password))

    def test_display_password(self):
        """
        Here it checks weather the display_Password function will return the password in the password list
        """
    def save_password(self):
        self.new_password.save_password()
        new_pass = Password("facebook", "2017")
        new_pass.save_password()
        self.assertEqual(len(Password.password),
                         len(Password.display_passwords()))

    def test_delete(self):
        """
        This test will check whether the password gets deleted from the passwords list
        """
        self.new_password.save_password()
        new_password = Password("facebook", "2017")
        new_password.save_password()
        Password.delete_password("instagram")
        self.assertEqual(len(Password.password_list), 1)

    def test_password_exist(self):
        """
        This will check whether the password_exists function works
        """
        self.new_password.save_password()
        self.assertTrue(Password.password_exist("instagram"))


if __name__ == "__main__":
    unittest.main()
