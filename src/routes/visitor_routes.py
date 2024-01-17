from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.controllers.user import Visitor

blp = Blueprint('visitor', __name__, description='operations performed by a visitor')


@blp.route('/issues/<string:name>')
class IssueBook(MethodView):
    def post(self, name):
        issued = Visitor().issue_book(name)
        if issued:
            return {"message": f"Book {name} issued successfully!"}, 200
        abort(404, message='Book not found')


@blp.route('/issues/<string:username>')
class BooksIssued(MethodView):
    def get(self, username):
        issued = Visitor().books_issued()
        if issued:
            return {"books": issued}, 200
        abort(404, message="Books not issued")
