from app.extinsions import db
from app.main import main
from app.post.models import Post
from flask import render_template
from flask_login import current_user, login_required

@main.route('/')
@login_required
def home():
    posts = Post.query.all()
    return render_template('index.html',posts=posts)

@main.route('/like-unlike/<int:post_id>')
@login_required
def like_unlike(post_id):
    post=Post.query.get_or_404(post_id)
    if post not in current_user.posts_liked.all():
        current_user.posts_liked.append(post)
    else :
        current_user.posts_liked.remove(post)
    db.session.commit()
    return '', 200
