from flask_restful import fields, marshal_with, Resource, reqparse
from flask import request
from ..models import User, Post, Comment, Like
from .validation import BusinessValidationError
from ..database import db
from flask_jwt_extended import jwt_required, current_user

post_fields = {
    "id": fields.Integer,
    "author_id": fields.Integer,
    "title": fields.String,
    "description": fields.String,
}

comment_fields = {
    "id":fields.Integer,
    "author_id": fields.Integer,
    "post_id": fields.Integer,
    "created_at": fields.DateTime,
    "content": fields.String
}

like_fields = {
    "id": fields.Integer,
    "post_id": fields.Integer,
    "author_id": fields.Integer
}


create_comment_parser = reqparse.RequestParser()
create_comment_parser.add_argument("content",location='form')
create_comment_parser.add_argument("author_id",location='form')

like_parser = reqparse.RequestParser()
like_parser.add_argument("author_id",location='form')

class PostAPI(Resource):

    @marshal_with(post_fields)
    def get(self,post_id):
        post = Post.query.filter(Post.id == post_id).first()
        if not post:
            raise BusinessValidationError(status_code=404, error_code="P1",error_message="Post does not exist")
        return post


    @jwt_required()
    def post(self):
        author_id = current_user.id
        title, description = self.json['title'], self.json['description']
        print(title,description)
        if not author_id:
            raise BusinessValidationError(
                status_code=400,
                error_code="P2",
                error_message="Author ID is required"
            )
        if not title:
            raise BusinessValidationError(
                status_code=400,
                error_code="P3",
                error_message="title is required"
            )
        if not description:
            raise BusinessValidationError(
                status_code=400,
                error_code="P4",
                error_message="description is required"
            )

        author = User.query.filter(User.id == author_id).first()
        if not author:
            raise BusinessValidationError(
                status_code=400,
                error_code="P5",
                error_message="Author ID does not exist"
            )

        new_post = Post(author_id=author_id, title=title, description=description)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @marshal_with(post_fields)
    def put(self, post_id):
        post,title, description, author_id = None

        post = Post.query.filter(Post.id == post_id).first()
        user = User.query.filter(User.id == author_id).first()

        if not post:
            raise BusinessValidationError(
                status_code=400,
                error_code="P6",
                error_message="Invalid Post"
            )

        if not user:
            raise BusinessValidationError(
                status_code=400,
                error_code="P7",
                error_message="Invalid User"
            )

        if post.user.id != user.id:
            raise BusinessValidationError(
                status_code=401,
                error_code="P8",
                error_message="Author has not made the post"
            )

        if not description and not title:
            raise BusinessValidationError(
                status_code=400,
                error_code="P9",
                error_message="Title and content cannot be empty"
            )

        post.description = description
        post.title = title
        db.session.commit()

    @marshal_with(post_fields)
    def delete(self, post_id):
        post = Post.query.filter(Post.id == post_id).first()

        if not post:
            raise BusinessValidationError(
                status_code=400,
                error_code="P10",
                error_message="Invalid Post"
            )

        for like in post.likes:
            db.session.delete(like)
        for comment in post.comments:
            db.session.delete(comment)

        db.session.delete(post)
        db.session.commit()
        return post

class CommentAPI(Resource):

    @marshal_with(comment_fields)
    def post(self,post_id):
        args = create_comment_parser.parse_args()
        author_id = args.get("author_id",None)
        content = args.get("content",None)

        post = Post.query.filter(Post.id == post_id).first()
        if not post:
            raise BusinessValidationError(status_code=400,error_code="C1",error_message="Invalid Post ID")

        if not content:
            raise BusinessValidationError(status_code=400,error_code="C2",error_message="Content field required")
        
        if not author_id:
            raise BusinessValidationError(status_code=400,error_code="C3",error_message="Author field required")

        new_comment = Comment(content=content,author=author_id,post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
        return new_comment

class LikeAPI(Resource):

    @marshal_with(like_fields)
    def post(self, post_id):
        args = like_parser.parse_args()
        author_id = args.get("author_id",None)
        if not author_id:
            raise BusinessValidationError(status_code=400,error_code="L1",error_message="Author ID required")

        post = Post.query.filter(Post.id == post_id).first()
        if not post:
            raise BusinessValidationError(status_code=400,error_code="L2",error_message="Invalid Post ID")

        like = Like.query.filter(Like.author_id == author_id and Like.post_id == post_id).first()

        if like:
            db.session.delete(like)
        else:
            like = Like(author_id=author_id, post_id=post_id)
            db.session.add(like)
        db.session.commit()

        return like





        
