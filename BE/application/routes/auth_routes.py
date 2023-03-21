from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, make_response, current_app, json
import datetime
import datetime
from flask_login import login_user, login_required, logout_user, current_user
from ..database import db
from ..models import User
import jwt
import requests
from functools import wraps

auth = Blueprint("auth", __name__)

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user = User.query.filter_by(username=data['id']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

@auth.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        print("got post request at login")
        data = request.json
        username = data["username"]
        password = data["password"]

        print(username,password)

        #remember = True if request.get('remember') else False

        user = User.authenticate(username=username,password=password)

        if not user:
            return make_response('Could not verify',401)
        else:
            token = jwt.encode({'id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, current_app.config['SECRET_KEY'],algorithm="HS256")

            print(f"generated token {token}")
            return make_response(jsonify({'token' : token}),200)

    
    else:
        if current_user.is_authenticated:
            print("here")
            return redirect(url_for('main.home'))
        return render_template("login.html")



@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.json
        username = data["username"]
        password = data["password"]
        name = data["name"]

        res = requests.post(request.host_url+"api/user",{
            "username":username,
            "name":name,
            "password":password
        })
        if res.status_code == 400:
            print(res.json())
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
