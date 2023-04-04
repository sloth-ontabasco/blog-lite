from flask_restful import  marshal_with, Resource
import os
from flask import jsonify
from ..models import User, Post, Comment, Like, followers
from .validation import BusinessValidationError
from ..database import db
from flask_jwt_extended import jwt_required, current_user
from .utils import post_fields, comment_fields, like_fields, create_comment_parser, like_parser, create_post_parser 


class PostAPI(Resource):

    def get(self, post_id):
        post = Post.query.filter(Post.id == post_id).first()
        if not post:
            raise BusinessValidationError(status_code=404, error_code="P1",error_message="Post does not exist")

        res = post.to_dict()
        return jsonify(post.to_dict())


    @jwt_required()
    def post(self):
        author_id = current_user.id

        args = create_post_parser.parse_args()
        img = args.get("image",None)
        description = args.get("description",None)
        title = args.get("title",None)

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

        img.save(f"templates/static/blog_pictures/{new_post.id}.png")
        return new_post.to_dict()

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

class HomeAPI(Resource):

    @jwt_required()
    def get(self):
        followed_posts = Post.query.join(
            followers, (followers.c.followed_id == Post.author_id)
        ).filter(followers.c.follower_id == current_user.id)
        own_posts = Post.query.filter_by(author_id=current_user.id)

        if not followed_posts.all():
            print("no following posts")
            if own_posts.all():
                print("POSTS TO DISPLAY FOR " + current_user.username)
                appearing_posts = Post.query.filter_by(author_id=current_user.id).order_by(Post.created_on.desc()).limit(15).all()
            else:
                print("NO POST TO DISPLAY FOR " + current_user.username)
                return None
        else:
            if own_posts.first():
                appearing_posts = followed_posts.union(own_posts).order_by(Post.created_on.desc()).limit(15).all()
            else:
                appearing_posts = followed_posts.order_by(Post.created_on.desc()).limit(15).all()

        
        return [appearing_post.to_dict() for appearing_post in appearing_posts]

class CommentAPI(Resource):
    """
    Route: /api/post/:post_id/comment
    """

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

    def get(self, post_id):
        post = Post.query.filter(Post.id == post_id).first()
        if not post:
            raise BusinessValidationError(status_code=400,error_code="C1",error_message="Invalid Post ID")

        if not post.comments:
            return []
        
        comments = []
        for comment in post.comments:
            comments.append(comment.to_dict())

        return comments

        

class LikeAPI(Resource):
    """
    Route: /api/post/:post_id/like
    """

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

    def get(self,post_id):
        post = Post.query.filter(Post.id == post_id).first()
        if not post:
            raise BusinessValidationError(status_code=400,error_code="L2",error_message="Invalid Post ID")

        if not post.likes: 
            return []
        
        liked_users = []
        for like in post.likes:
            liked_users.append(like.user.to_dict())

        return liked_users
