import os
from app.extinsions import db
from app.user import user
from app.user.models import User
from app.user.forms import SignupForm, LoginForm, ResetForm, PasswordResetForm, SettingForm
from app.helper.mail import send_email
from app.helper.pics import save_picture
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required

basedir = os.path.abspath(os.path.dirname(__file__))

@user.route('/<username>')
def home(username):
    if not current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user=User.query.filter_by(username = username).first_or_404()
    return render_template('user.html', user=user)

@user.route('un_follow/<username>')
def un_follow(username):
    if not current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user=User.query.filter_by(username = username).first_or_404()
    if current_user.is_following(user):
        current_user.unfollow(user)
        flash(f'You have unfollowed {user.username}', 'info')
    else :
        current_user.follow(user)
        flash(f'You have followed {user.username}', 'info')
    db.session.commit()
    return redirect(url_for('user.home', username = user.username))

@user.route('<username>/followers')
def user_followers(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_users.html', users = user.all_followers)

@user.route('<username>/followed')
def user_followed(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('show_users.html', users = user.all_followed)

@user.route('/setting', methods=['GET', 'POST'])
def setting():
    if not current_user.is_authenticated and not current_user.is_confirmed:
        return redirect(url_for('main.home'))
    form = SettingForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.avatar.data :
             f=form.avatar.data
             name = save_picture(f, os.path.join(basedir, 'static/images'))
             current_user.avatar = name
        flash(f'Your details have been changed', 'info')
        db.session.commit()
        return redirect(url_for('user.home', username=current_user.username))
    form.username.data = current_user.username
    form.name.data = current_user.name
    form.email.data = current_user.email
    return render_template('setting.html', form=form)

@user.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return 'you need to logout to access this page'
    form = SignupForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, username=form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        user.self_follow
        db.session.commit()
        login_user(user, remember=True)
        flash(f'Account has been created for { user.username } please confirm your e-mail', 'success')
        return redirect(url_for('user.confirm'))
    return render_template('signup.html', form=form)

@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return 'you need to logout to access this page'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        if user and user.check_password(form.password.data) :
            login_user(user, remember=True)
            flash(f'You are logged in', 'success')
            return redirect(url_for('main.home'))
    return render_template('login.html', form=form)

@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login')) 

@user.route('/confirm')
@login_required
def confirm():
    if current_user.is_confirmed:
        return 'you are already confirmed'
    token = current_user.get_serializer_token(salt='e-mail confirmation')
    send_email(subject = 'e-mail confirmation',
               to = current_user.email,
               text_body = 'if you are getting this it means you are unable to see html page please contact admin',
               template = 'confirm',
               token = token)
    return '<h1>An confirmation mail has been send to e-mail. Check your inbox</h1>'

@user.route('/confirm/<token>')
@login_required
def confirmation(token):
    if current_user.is_confirmed:
        return 'you are already confirmed'
    user = User.verify_serializer_token(token, salt='e-mail confirmation')
    if user:
        user.is_confirmed = True
        db.session.commit()
        return f'<h1>{user.username}your email has been confirmed now you can post images</h1>'
    return "<h1>There has been some issue please try again</h1>"

@user.route('/reset', methods=['GET', 'POST'])
def reset():
    if current_user.is_authenticated:
        return 'you need to logout to access this page'
    form = ResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user :
            token = user.get_serializer_token(salt='password reset')
            send_email(subject = 'password reset',
                       to = user.email,
                       text_body = 'if you are getting this it means you are unable to see html page please contact admin',
                       template = 'reset',
                       token = token)
            return '<h1>Mail has been send. Check your inbox</h1>'
    return render_template('reset.html', form=form)

@user.route('reset/<token>', methods=['GET', 'POST'])
def reset_request(token):
    if current_user.is_authenticated:
        return 'you need to logout to access this page'
    form = PasswordResetForm()
    user = User.verify_serializer_token(token, salt='password reset')
    if user:
        if form.validate_on_submit():
            user.set_password(form.password.data)
            db.session.commit()
            return redirect(url_for('user.login'))
        return render_template('password_reset.html', form=form)
    else :
        return redirect(url_for('user.reset'))
    return "password Reset Request"
