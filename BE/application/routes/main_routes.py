from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_required, current_user
from ..models import Post, followers, User
from ..api.validation import NotFoundError
import requests

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return redirect(url_for("main.home"))


@main.route("/home")
@login_required
def home():

    followed_posts = Post.query.join(
        followers, (followers.c.followed_id == Post.author_id)
    ).filter(followers.c.follower_id == current_user.id)
    own_posts = Post.query.filter_by(author_id=current_user.id)

    if not followed_posts.all():
        print("no following posts")
        if own_posts.all():
            appearing_posts = Post.query.filter_by(author_id=current_user.id).order_by(Post.created_on.desc()).limit(15)
        else:
            return render_template("home.html", posts=None)
    else:
        if own_posts.first():
            appearing_posts = followed_posts.union(own_posts).order_by(Post.created_on.desc()).limit(15)
        else:
            appearing_posts = followed_posts.order_by(Post.created_on.desc()).limit(15)
    
    return render_template("home.html",posts=appearing_posts.all())

 
@main.route("/users/<int:user_id>", methods=["GET"])
@login_required
def profile(user_id):
    user = User.query.filter(User.id == user_id).first()
    if not user:
        raise NotFoundError(404)

    posts = Post.query.filter_by(author_id=user.id).all()
    return render_template("profile.html",user=user,posts=posts)


@main.route("/users/<int:user_id>/edit", methods=["POST"])
@login_required
def edit_profile(user_id):
    username = request.form.get("username",None)
    name = request.form.get("name",None)
    password = request.form.get("password-id", None)
    author_id = request.form.get("author_id",None)

    res = requests.put(request.host_url + f"api/user/{username}",{
        "username": username,
        "name":name,
        "password":password,
        "author_id": current_user.id
    })
    print(res.json())

    if res.status_code == 200:
        flash("success")
        return redirect(f"/users/{res.json()['id']}")
    else:
        flash("Uh oh, your post could not be edited")
        return redirect(f"{request.url_root}")



