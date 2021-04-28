from flask import Flask
from app.extinsions import db, migrate, login_manager, mail, dropzone
from app.commands import create_tables
from app.user import user
#from app.user.models import User
from app.main import main
from app.post import post
#import flask_whooshalchemy as wa

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    dropzone.init_app(app)
    #csrf.init_app(app)
#    wa.whoosh_index(app, User)

    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(post, url_prefix='/post')
    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app
