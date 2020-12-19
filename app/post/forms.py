from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    caption = StringField('cation')
    images = HiddenField('images', validators=[DataRequired('You must Upload Atleast one image')])
    submit = SubmitField('Add Post')

