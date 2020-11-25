from threading import Thread
from flask import render_template, current_app
from flask_mail import Message
from app import mail


def send_async_email(app, msg):
        with app.app_context():
            mail.send(msg)


def send_email(template, subject='', to='',
               text_body='', sync=False, **kwargs):
    msg = Message(current_app.config['MAIL_SUBJECT_PREFIX']+subject, recipients=[to])
    msg.body = text_body
    msg.html = render_template(f'mail/{template}.html', **kwargs)
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_email,
               args=(current_app._get_current_object(), msg)).start()
