import os
from app.extinsions import db
from app.post import post
from app.post.forms import PostForm
from app.post.models import Post
from app.helper.pics import save_picture
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required

basedir = os.path.abspath(os.path.dirname(__file__))

@post.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(images=form.images.data, caption=form.caption.data, user=current_user)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('new.html', form=form)

@post.route('/upload-images', methods = ['POST'])
def upload_image():
    if request.method == 'POST':
        names =[]
        for key, f in request.files.items():
            if key.startswith('file'):
                name = save_picture(f, os.path.join(basedir, 'static/images'))
                names.append(name)
        return jsonify(images = str(names))
