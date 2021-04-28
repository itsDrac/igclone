from app.extinsions import db
from flask.cli import with_appcontext
import click

@click.command(name="create_db")
@with_appcontext
def create_tables():
    db.create_all()

@click.command(name="drop_db")
@with_appcontext
def create_tables():
    db.drop_all()
