from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from ..database import db
from ..models import User
import requests

auth = Blueprint("auth", __name__)


@auth.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(username=username).first()

        if not user or not password == user.password:
            return redirect(url_for('auth.login')) 

        login_user(user, remember=remember)
        return redirect(url_for('main.home'))
    
    else:
        if current_user.is_authenticated:
            return redirect(url_for('main.home'))
        return render_template("login.html")


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password")

        res = requests.post(request.host_url+"api/user",{
            "username":username,
            "name":name,
            "password":password
        })
        if res.status_code == 400:
            if res.json()['error_code'] == 'U4':
                return render_template('register.html',user_exists=True)

        img = request.files.get("file-upload")
        if img:
            img.save(f"templates/static/profile_pictures/{res.json()['id']}.png")
        flash("Registation successful, please login")
        return redirect(url_for("auth.login"))
    else:
        return render_template("register.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
