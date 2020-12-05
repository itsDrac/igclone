import os
from app.extinsions import db
from app.post import post
from app.post.forms import PostForm
from app.post.models import Post, Image
from app.helper.pics import save_picture
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

basedir = os.path.abspath(os.path.dirname(__file__))

@post.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(caption=form.caption.data, user=current_user)
        for key, f in request.files.items():
            if key.startswith('file'):
                name = save_picture(f, os.path.join(basedir, 'static/images'))
                img = Image(name=name)
                p.images.append(img)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('new.html', form=form)

