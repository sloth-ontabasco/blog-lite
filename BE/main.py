from functools import wraps
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from application.models import User
from application.database import db
from application.config import LocalDevelopmentConfig
from application.routes.main_routes import main as main_bp
from application.routes.auth_routes import auth as auth_bp
from application.routes.post_routes import post as post_bp
from application.api.post_api import *
from application.api.user_api import *
from flask_jwt_extended import JWTManager
import logging

logger = logging.basicConfig()
app, api = None, None

def create_app(): 
    app = Flask(__name__, template_folder='templates',static_folder='templates/static')
    CORS(app)
    app.config.from_object(LocalDevelopmentConfig)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)
    db.init_app(app)

    jwt = JWTManager(app) 
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        user = User.query.filter_by(username=identity).one_or_none()
        return user 


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(int(_id))

    api = Api(app)
    with app.app_context():
        db.create_all()

    return app, api

app, api = create_app() 
bcrypt = Bcrypt(app)

api.add_resource(UserAPI, "/api/user","/api/user/<string:username>")
api.add_resource(SearchAPI,"/api/users/<string:search_str>")
api.add_resource(FollowAPI, "/api/user/follow/<string:follower>")
api.add_resource(UnollowAPI, "/api/user/unfollow/<string:follower>")

api.add_resource(PostAPI,"/api/post", "/api/post/<int:post_id>")
api.add_resource(CommentAPI, "/api/post/<int:post_id>/comment")
api.add_resource(LikeAPI,"/api/post/<int:post_id>/like")

if __name__ == '__main__':
    app.run(port=8081)
