from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from src.controllers.book import Book
from src.schemas import BookSchema
from src.utils.rbac import restricted
from src.controllers.user import Librarian
from src.config.constants import authorization_bearer

blp = Blueprint('Librarian', __name__, description='Routes for librarian')


# @blp.arguments(BookSchema)
@blp.route('/books')
class AddBook(MethodView):
    @restricted('librarian')
    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    @blp.arguments(BookSchema)
    def post(self, book_data):
        book_obj = Book(book_data['name'], book_data['author'], book_data['rating'], book_data['price'],
                        book_data['genre'])
        book_added = book_obj.add_book()
        if book_added:
            return {"message": f"Book added {book_obj.name}"}, 200
        return {"message": "Something went wrong"}, 400


@blp.route('/books/<string:book_name>')
class RemoveBook(MethodView):
    @restricted('librarian')
    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def delete(self, book_name):
        status = Librarian().remove_book(book_name)
        if status:
            return {"message": f"Book {book_name} is removed"}, 200
        abort(404, message=f"Book with name {book_name} not found!")

