from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class PostForm(FlaskForm):
    caption = StringField('cation')
    submit = SubmitField('Add Post')

