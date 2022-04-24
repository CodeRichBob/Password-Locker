import unittest #importing unittest module
from credential import Credential  #importing credential class

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Arg:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Robert", "Gitonga", "Coderichbob", "robert123", "robert@ms.com") # New Credential

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name, "Robert")
        self.assertEqual(self.new_credential.last_name, "Gitonga")
        self.assertEqual(self.new_credential.user_name, "CodeRichBob")
        self.assertEqual(self.new_credential.password, "robert123")
        self.assertEqual(self.new_credential.email, "robert@ms.com")

    def test_save_credential(self):
        '''
        Test if credential object is saved in credential_list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credential_list), 1) #save new credential

    def test_save_multiple_credential(self):
        '''
        Check if we can save multiple credential into the credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Robert", "Gitonga", "CodeRichBob", "robert123", "robert@ms.com")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_delete_credential(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Robert", "Gitonga", "CodeRichBob", "robert123", "robert@ms.com")
        test_credential.save_credential()

        self.new_credential.delete_credential() #Deleting credential
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credentials_by_email(self):
        '''
        test to check if we can find a credentials by email and display information
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Robert", "Gitonga", "CoderichBob", "robert123", "robert@ms.com")
        test_credential.save_credential()
        found_credential = Credential.find_email("robert@ms.com")
        self.assertEqual(found_credential.first_name, test_credential.first_name)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credentials
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Robert", "Gitonga", "CoderichBob", "robert123", "robert@ms.com")
        test_credential.save_credential()

        credentials_exists = Credential.credential_exit("robert@ms.com")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()