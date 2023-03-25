from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    jsonify,
    make_response,
    current_app,
    json,
)
from flask_login import login_required, logout_user, current_user
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
import requests
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
)
from ..database import db
from ..models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print("got post request at login")
        data = request.json
        username = data["username"]
        password = data["password"]

        print(username, password)

        # remember = True if request.get('remember') else False

        user = User.authenticate(username=username, password=password)

        if not user:
            return make_response("Could not verify", 401)
        else:
            token = create_access_token(identity=user.username)
            ref_token = create_refresh_token(identity=user.username)
            print(token)
            return jsonify({"token": token, "ref_token": ref_token}), 200


@auth.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    username = get_jwt_identity()
    access_token = create_access_token(identity=username)
    return (jsonify(access_token=access_token),200)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.json
        username = data["username"]
        password = data["password"]
        name = data["name"]

        res = requests.post(
            request.host_url + "api/user",
            {"username": username, "name": name, "password": password},
        )
        if res.status_code == 400:
            print(res.json())
            if res.json()["error_code"] == "U4":
                return render_template("register.html", user_exists=True)

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
    return redirect(url_for("main.index"))
