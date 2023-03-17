from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..database import db
from ..models import User, Post, Like
import requests

post = Blueprint("post", __name__)

@post.route("/post",methods=["POST"])
@login_required
def make_post():
    author_id = current_user.id
    title = request.form.get("title")
    description = request.form.get("content")

    res = requests.post(request.host_url+"api/post",{
        "author_id":author_id,
        "title":title,
        "description":description
    })
    if res.status_code == 200:
        img = request.files.get("file-upload")
        img.save(f"templates/static/blog_pictures/{res.json()['id']}.png")
        return redirect(url_for("main.home"))
    else:
        flash("Uh oh your post could not be made, try again")

@post.route("/posts/<int:post_id>",methods=["GET"])
@login_required
def view_post(post_id):
    res = requests.get(request.host_url + f"api/post/{post_id}")
    if res.status_code != 200:
        flash("Post doesnt exist")
        return redirect(url_for('main.home'))
    post = Post.query.filter(Post.id == post_id).first()
    liked = Like.query.filter(Like.post_id == post.id, Like.author_id == current_user.id).count() > 0
    num_likes = len(post.likes)

    return render_template("post.html", post=post, liked=liked, num_likes=num_likes)
    
@post.route("/edit",methods=["POST"])
@login_required
def edit_post():
    author_id = current_user.id 
    title = request.form.get("title",None)
    content = request.form.get("content",None)
    post_id = request.form.get("post-id", None)

    res = requests.put(request.host_url + f"api/post/{post_id}",{
        "author_id": author_id,
        "title":title,
        "description":content
    })

    if res.status_code == 200:
        return redirect(f"/posts/{post_id}")
    else:
        flash("Uh oh, your post could not be edited")
        return redirect(f"/posts/{post_id}")


@post.route("/delete",methods=["POST"])
@login_required
def del_post():
    post_id = request.form.get("post-id",None)
    res = requests.delete(request.host_url + f"api/post/{post_id}")

    if res.status_code == 200:
        flash("Post has been successfully deleted")
        return redirect(url_for("main.home"))
    else:
        flash("Uh oh, the post could not be deleted")
        return redirect(f"/posts/{post_id}")