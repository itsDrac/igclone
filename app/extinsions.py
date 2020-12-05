from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_dropzone import Dropzone
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please Login to access this page"
login_manager.login_message_category = "warrning"

mail = Mail()

dropzone = Dropzone()

csrf = CSRFProtect()
