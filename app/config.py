from secrets import token_hex
import os

SECRET_KEY = token_hex(16)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////'+ os.path.abspath(os.getcwd()) + '/Database/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
MAIL_SERVER= 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_SUBJECT_PREFIX = 'Ig-Clone : '
MAIL_DEFAULT_SENDER = 'Drac From ig-clone'
