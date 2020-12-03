from app.main import main
from flask import render_template
from flask_login import current_user, login_required

@main.route('/')
@login_required
def home():
    return render_template('index.html')
