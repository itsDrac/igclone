from secrets import token_hex
import os

SECRET_KEY = token_hex(16)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////'+ os.path.abspath(os.getcwd()) + '/Database/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
