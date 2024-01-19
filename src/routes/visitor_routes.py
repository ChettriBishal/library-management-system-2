from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from src.controllers.user import Visitor
from src.schemas import BookNameSchema
from src.config.constants import authorization_bearer

blp = Blueprint('visitor', __name__, description='operations performed by a visitor')


@blp.route('/issues/')
class IssueBook(MethodView):

    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    @blp.arguments(BookNameSchema)
    def post(self, data):
        issued = Visitor().issue_book(data["name"])
        if issued:
            return {"message": f"Book {data['name']} issued successfully!"}, 200
        else:
            abort(404, message='Book not found')


@blp.route('/issues')
class BooksIssued(MethodView):
    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def get(self):
        issued = Visitor().books_issued()
        if issued:
            return {"books": issued}, 200
        else:
            abort(404, message="Books not issued")
