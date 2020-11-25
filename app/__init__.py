from flask import Flask
from app.extinsions import db, migrate, login_manager
from app.user import user

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(user, url_prefix='/user')

    return app
