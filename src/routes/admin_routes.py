from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required, get_jwt
from flask import request
from src.schemas import UserSchema
from src.controllers.authentication import Authentication
from src.blocklist import BLOCKLIST
from src.utils.rbac import restricted
from src.controllers.user import Admin
from src.config.constants import authorization_bearer

blp = Blueprint("Admin", __name__, description="Operation performed via admin")


@blp.route('/admin/users')
class ListUsers(MethodView):
    @restricted('admin')
    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def get(self):
        admin_obj = Admin()
        return admin_obj.get_users(), 200


@blp.route('/user/<string:user_name>')
class RemoveUser(MethodView):
    @restricted('admin')
    @jwt_required()
    @blp.doc(parameters=authorization_bearer)
    def delete(self, user_name):
        admin_obj = Admin()
        user_removed = admin_obj.remove_user(user_name)
        if user_removed:
            return {"message": f"{user_name} removed"}, 200


@blp.route('/register/librarian')
class RegisterLibrarian(MethodView):
    @blp.arguments(UserSchema)
    @blp.doc(parameters=authorization_bearer)
    def post(self, user_data):
        auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
        signed_up = auth.signup()
        if signed_up:
            return {"message": f"Librarian {user_data['username']} registered, uuid {signed_up}"}
        return {"message": "choose different username"}, 409
