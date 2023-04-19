from flask_restful import fields, reqparse
import werkzeug

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

get_user_parser = reqparse.RequestParser()
get_user_parser.add_argument('ff_only', default=False, required=False, type=bool, help='blablabla')

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument("username", location="form")
create_user_parser.add_argument("name", location="form")
create_user_parser.add_argument("password", location="form")

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument("username", location="form")
update_user_parser.add_argument("password", location="form")
update_user_parser.add_argument("name", location="form")
update_user_parser.add_argument("author_id", location="form")

create_post_parser = reqparse.RequestParser()
create_post_parser.add_argument("title",location="form")
create_post_parser.add_argument("description",location="form")
create_post_parser.add_argument("image",type=werkzeug.datastructures.FileStorage,location="files")

update_post_parser = reqparse.RequestParser()
update_user_parser.add_argument("title",location="json")
update_user_parser.add_argument("description",location="json")

create_follow_parser = reqparse.RequestParser()
create_follow_parser.add_argument("username",location="form")

create_comment_parser = reqparse.RequestParser()
create_comment_parser.add_argument("content",location='form')
create_comment_parser.add_argument("author_id",location='form')

like_parser = reqparse.RequestParser()
like_parser.add_argument("author_id",location='form')