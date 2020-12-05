from app.extinsions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    caption = db.Column(db.String(50))
    images = db.relationship('Image', backref='post', lazy='dynamic')

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

