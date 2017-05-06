import unittest

from app import app


class ProjectTests(unittest.TestCase):
    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEquals(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ########################
    #### helper methods ####
    ########################



    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Home', response.data)
        self.assertIn(b'Services', response.data)
        self.assertIn(b'Contact', response.data)
        self.assertIn(b'Login', response.data)


if __name__ == "__main__":
    unittest.main()