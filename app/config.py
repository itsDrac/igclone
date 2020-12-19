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
DROPZONE_DEFAULT_MESSAGE = 'Drop or Click to upload <br> (max 3 files can be uploaded)'
DROPZONE_ALLOWED_FILE_TYPE='image'
DROPZONE_MAX_FILE_SIZE=5
DROPZONE_MAX_FILES=3
DROPZONE_UPLOAD_ON_CLICK=True
DROPZONE_IN_FORM=True
DROPZONE_ENABLE_CSRF=True
DROPZONE_UPLOAD_MULTIPLE=True
DROPZONE_PARALLEL_UPLOADS=3
DROPZONE_UPLOAD_BTN_ID='submit'
DROPZONE_UPLOAD_ACTION='post.upload_image'
