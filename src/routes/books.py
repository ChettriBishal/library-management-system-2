from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from src.schemas import BookSchema
from src.controllers.authentication import Authentication

blp = Blueprint("Books", __name__, description="Operation on books")


@blp.route('/user/books')
class Books(MethodView):
    @jwt_required()
    @blp.response(200, BookSchema)
    def get(self):
        return {"books": "DEMO"}
