from flask_restful import fields, reqparse

user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "name": fields.String,
    "created_on": fields.DateTime
}
 
post_fields = {
    "id": fields.Integer,
    "author": fields.Nested(user_fields),
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

create_comment_parser = reqparse.RequestParser()
create_comment_parser.add_argument("content",location='form')
create_comment_parser.add_argument("author_id",location='form')

like_parser = reqparse.RequestParser()
like_parser.add_argument("author_id",location='form')