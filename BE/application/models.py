from dataclasses import dataclass
from .database import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from flask_restful import fields
from flask_bcrypt import generate_password_hash, check_password_hash
from typing import Mapping

followers = db.Table(
    "followers",
    db.Column("follower_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("user.id")),
)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String(100))
    followed = db.relationship(
        "User",
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref("followers",lazy='dynamic'),
        lazy='dynamic'
    )
    posts = db.relationship("Post", backref="user",lazy='dynamic')
    comments = db.relationship("Comment",backref="user",lazy='dynamic') 
    likes = db.relationship("Like",backref="user",lazy='dynamic')

    def __init__(self, username=username, password=password, name=name):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name

    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        print(f"authenticating with {username} and {password}") 
        if not username or not password:
            return None

        user = cls.query.filter_by(username=username).first()
        if not check_password_hash(user.password, password):
            print("failed pass hash")
            return None

        return user


    # define methods for reusability
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "followed": [followed.to_dict() for followed in self.followed]
        }


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=func.now())
    comments = db.relationship("Comment", backref="post")
    likes = db.relationship("Like", backref="post")

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.user.to_dict(),
            "title": self.title,
            "description": self.description,
            "created_on": self.created_on.strftime(format="%H:%M %d/%m/%Y")
        }

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text)
    created_on = db.Column(db.DateTime, server_default=func.now())
    author = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))


class Like(db.Model):
    __tablename__ = "like"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
