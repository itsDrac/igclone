import os
from app.extinsions import db
from app.post import post
from app.post.forms import PostForm, CommentForm
from app.post.models import Post, Comment
from app.helper.pics import save_picture
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_required

basedir = os.path.abspath(os.path.dirname(__file__))

@post.route('/<int:post_id>', methods = ['GET', 'POST'])
def home(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404()
    form = CommentForm()
    if form.validate_on_submit() and current_user.is_authenticated:
        if current_user not in [ comment.user for comment in post.comments.all() ]:
            com = Comment(user_id=current_user.id, post_id=post.id, body=form.body.data)
            db.session.add(com)
            db.session.commit()
        return redirect(url_for('post.home', post_id=post.id))
    return render_template('post.html', post=post, form=form)

@post.route('/new', methods = ['GET', 'POST'])
@login_required
def new():
    if not current_user.is_authenticated and not current_user.is_confirmed:
        return redirect(url_for('main.home'))
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
