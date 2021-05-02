import ast, os
from app.extinsions import db
from sqlalchemy.event import listens_for

basedir = os.path.abspath(os.path.dirname(__file__))

likes = db.Table('likes',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
                 )

class Comment(db.Model):
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True)
    body = db.Column(db.String(50))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    caption = db.Column(db.String(50))
    images = db.Column(db.String(100), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    get_images = lambda self : ast.literal_eval(self.images)


@listens_for(Post, "after_delete")
def delete_images(mapper, connection, target):
    for image in target.get_images():
        try :
            os.remove(os.path.join(basedir, 'static/images/', image))
        except OSError:
            pass
