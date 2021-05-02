from app.extinsions import db
from app.user.models import User
from flask.cli import with_appcontext
import click

@click.command(name="create_db")
@with_appcontext
def create_tables():
    db.create_all()

@click.command(name="drop_db")
@with_appcontext
def delete_tables():
    db.drop_all()

@click.command(name="del_unauth_user")
@with_appcontext
def del_user():
    def comments(user):
        for comment in user.comments.all():
            db.session.delete(comment)

    def posts(user):
        for post in user.posts.all():
            db.session.delete(post)

    for user in User.query.all():
        if not user.is_confirmed :
            comments(user)
            posts(user)
            db.session.delete(user)

    db.session.commit()

