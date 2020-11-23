from app.user.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError

class SignupForm(FlaskForm):
        name = StringField('name', validators=[DataRequired()])
        username = StringField('username', validators=[DataRequired()])
        email = EmailField('E-mail', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired()])
        submit = SubmitField('Sign Up')

        def validate_email(self, email):
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This Email Is Already Taken')

        def validate_username(self, username):
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This Username Is Already Taken')
