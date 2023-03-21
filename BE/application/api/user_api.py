from flask_restful import fields, marshal_with, Resource, reqparse
from flask import request
from flask_login import current_user
import jwt
from ..models import User
from .validation import NotFoundError, BusinessValidationError
from ..database import db

user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "name": fields.String,
    "created_on": fields.DateTime
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument("username", location="form")
create_user_parser.add_argument("name", location="form")
create_user_parser.add_argument("password", location="form")

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument("username", location="form")
update_user_parser.add_argument("password", location="form")
update_user_parser.add_argument("name", location="form")
update_user_parser.add_argument("author_id", location="form")

create_follow_parser = reqparse.RequestParser()
create_follow_parser.add_argument("username",location="form")

class SearchAPI(Resource):
    """Search API"""
    def get(self, search_str):
        matching_users = (
            User.query.filter(User.username.like(f"%{search_str}%")).limit(10).all()
        )
        if not matching_users:
            raise BusinessValidationError(
                400, error_code="S1", error_message="No users found"
            )

        res = []
        for m in matching_users:
            if m == current_user:
                continue
            data = {"id": m.id,"name":m.name,"username":m.username}
            data['is_following'] = True if current_user.is_following(m) else False 
            res.append(data)

        return res


class UserAPI(Resource):
    # TODO add delete route
    @marshal_with(user_fields)
    def get(self, username):
        user = User.query(User.username == username).first()
        if user is None:
            raise NotFoundError(404)
        return user

    @marshal_with(user_fields)
    def post(self):
        print("reached here")
        args = create_user_parser.parse_args()
        username, name, password = (
            args.get("username", None),
            args.get("name", None),
            args.get("password", None),
        )

        if username is None:
            raise BusinessValidationError(
                status_code=400,
                error_code="U1",
                error_message="username is required",
            )

        if name is None:
            raise BusinessValidationError(
                status_code=400, error_code="U2", error_message="name is required"
            )

        if password is None:
            raise BusinessValidationError(
                status_code=400,
                error_code="U3",
                error_message="password is required",
            )

        user = User.query.filter(User.username == username).first()
        if user:
            raise BusinessValidationError(
                400, error_code="U4", error_message="User already exists"
            )
        new_user = User(username=username, name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @marshal_with(user_fields)
    def put(self, username):
        args = update_user_parser.parse_args()
        new_username, name, password, author_id = (
            args.get("username", None),
            args.get("name", None),
            args.get("password", None),
            args.get("author_id", None)
        )

        if not new_username and not name and not password:
            raise BusinessValidationError(
                status_code=400,
                error_code="U5",
                error_message="update is non existant",
            )

        user = User.query.filter(User.username == username).first()
        if not user:
            raise BusinessValidationError(
                status_code=400,
                error_code="U6",
                error_message="No user found to update",
            )

        if int(user.id) != int(author_id):
            raise BusinessValidationError(
                status_code=401,
                error_code="U7",
                error_message="Author ID not same as user ID"
            )

        existing_user = User.query.filter(User.username == new_username).first()
        if existing_user and new_username != username:
            raise BusinessValidationError(
                status_code=400,
                error_code="U8",
                error_message="User already exists",
            )

        if new_username:
            user.username = new_username
        if name:
            user.name = name
        if password:
            user.password = password

        db.session.commit()
        return user

    @marshal_with(user_fields)
    def delete(self, username):
        user = User.query.filter(User.username == username).first()
        if user is None:
            raise NotFoundError(404)
        
        for post in user.posts:
            for like in post.likes:
                db.session.delete(like)
            for comment in post.comments:
                db.session.delete(comment)
            db.session.delete(post)
            
        for like in user.likes:
            db.session.delete(like)

        for comment in user.comments:
            db.session.delete(comment)

        for f in user.followers:
            f.unfollow(user)

        for f in user.followed:
            user.unfollow(f)

        db.session.delete(user)
        db.session.commit()
        return user



class FollowAPI(Resource):

    @marshal_with(user_fields)
    def post(self, follower):
        args = create_follow_parser.parse_args()
        followed_str = args.get("username",None) 

        if not followed_str:
            raise BusinessValidationError(status_code=400,error_code="F1",error_message="Username is not found")


        follower = User.query.filter(User.username==follower).first()
        followed = User.query.filter(User.username==followed_str).first()

        if not follower: 
            raise BusinessValidationError(status_code=400,error_code="F2", error_message="Follower does not exist")
        
        if not followed:
            raise BusinessValidationError(status_code=400,error_code="F3",error_message="Followed does not exist")

        if followed == follower:
            raise BusinessValidationError(status_code=400, error_code="F4",error_message="Cannot follow self")

        follower.follow(followed)
        db.session.commit()
        return followed

class UnollowAPI(Resource):

    @marshal_with(user_fields)
    def post(self, follower):
        args = create_follow_parser.parse_args()
        followed_str = args.get("username",None) 

        if not followed_str:
            raise BusinessValidationError(status_code=400,error_code="UF1",error_message="Username is not found")


        follower = User.query.filter(User.username==follower).first()
        followed = User.query.filter(User.username==followed_str).first()

        if not follower: 
            raise BusinessValidationError(status_code=400,error_code="UF2", error_message="Follower does not exist")
        
        if not followed:
            raise BusinessValidationError(status_code=400,error_code="UF3",error_message="Followed does not exist")

        if followed == follower:
            raise BusinessValidationError(status_code=400, error_code="UF4",error_message="Cannot follow self")

        follower.unfollow(followed)
        db.session.commit()
        return followed
