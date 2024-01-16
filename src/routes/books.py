from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from src.controllers.book import Book
from src.controllers.user import User

from src.schemas import BookSchema
from src.controllers.authentication import Authentication

blp = Blueprint("Books", __name__, description="Operation on books")


@blp.route('/user/books')
class Books(MethodView):
    @jwt_required()
    @blp.response(200)
    def get(self):
        filter = request.args.get('filter')
        user_data_access = User()
        if filter == 'price':
            return user_data_access.sort_books_by_price()
        elif filter == 'rating':
            return user_data_access.sort_books_by_rating()
        # if request_data['']
        # return user_data_access.sort_books_by_rating()



