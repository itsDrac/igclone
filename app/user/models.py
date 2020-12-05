from app.extinsions import db, login_manager
from app.post.models import Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

class User(db.Model, UserMixin):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(200), unique=True, nullable=False)
        is_confirmed = db.Column(db.Boolean, default=False)
        posts = db.relationship('Post', backref='user', lazy='dynamic')

        def set_password(self, password):
            self.password = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password, password)

        def get_serializer_token(self, expires_sec=600, salt='default'):
            s = Serializer(current_app.config['SECRET_KEY'], expires_sec, salt=salt)
            return s.dumps({'user_id': self.id}).decode('utf-8')

        @staticmethod
        def verify_serializer_token(token, salt='default'):
            s = Serializer(current_app.config['SECRET_KEY'], salt=salt)
            try:
             user_id = s.loads(token)['user_id']
            except:
             return None
            return User.query.get(user_id)
