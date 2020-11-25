from app.extinsions import db
from app.user import user
from app.user.models import User
from app.user.forms import SignupForm, LoginForm
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user

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

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data) :
            login_user(user)
            return "User Loged In"
    return render_template('login.html', form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login')) 
