from app.extinsions import db
from werkzeug.security import generate_password_hash

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(200), unique=True, nullable=False)

        def set_password(self, password):
            self.password = generate_password_hash(password)
