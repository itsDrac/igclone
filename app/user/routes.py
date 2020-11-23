from app.extinsions import db
from app.user import user
from app.user.models import User
from app.user.forms import SignupForm
from flask import render_template

@user.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return "<h1>User Added</h1>"
    return render_template('signup.html', form=form)
