from flask import Flask
from app.extinsions import db, migrate, login_manager, mail, dropzone, csrf
from app.commands import create_tables, delete_tables, del_user
from app.user import user
from app.main import main
from app.post import post

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    dropzone.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(post, url_prefix='/post')
    app.register_blueprint(main)

    app.cli.add_command(create_tables)
    app.cli.add_command(delete_tables)
    app.cli.add_command(del_user)

    return app
