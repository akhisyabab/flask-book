import os


# grab the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control
SECRET_KEY = 'sembarang'
DEBUG = True


# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:password@localhost/flask_mantan_public'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Bcrypt algorithm hashing rounds
BCRYPT_LOG_ROUNDS = 15

WTF_CSRF_ENABLED = True

WHOOSH_ENABLED = os.environ.get('HEROKU') is None

#EMAIL SETTINGS
MAIL_SERVER='smtp.zoho.com'
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME = 'adminbantuin@zoho.com'
MAIL_PASSWORD = '123sanding'
MAIL_DEFAULT_SENDER = 'adminbantuin@zoho.com'
