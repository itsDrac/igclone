from app.extinsions import db
from app.main import main
from app.user.models import User
from app.post.models import Post
from app.post.forms import CommentForm
from flask import render_template, request
from flask_login import current_user, login_required

@main.route('/')
@login_required
def home():
    search = request.args.get('search', None)
    if search:
        users = User.query.msearch(search).all()
        return render_template('show_users.html', users = users)
    posts = current_user.followed_posts
    form = CommentForm()
    return render_template('index.html',posts=posts, form=form)

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

