# project/test_users.py


import unittest
import os

from app import app, db, mail
TEST_DB = 'user.db'


class ProjectTests(unittest.TestCase):
    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        mail.init_app(app)
        self.assertEquals(app.debug, False)
    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############
    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )

    def test_login_page(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertIn(b'masuk', response.data)

    def test_valid_login(self):
        self.app.get('/register', follow_redirects=True)
        self.app.get('akhi@gmail.com', 'p31234', 'p31234')
        self.app.get('/login', follow_redirects=True)
        response = self.login('akhi@gmail.com', 'p31234')


    def test_invalid_logout_within_being_logged_in(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'Log In', response.data)

    def test_user_registration_form_displays(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Create Account', response.data)


if __name__ == "__main__":
    unittest.main()