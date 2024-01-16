from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt
from flask import request
from src.schemas import UserSchema
from src.controllers.authentication import Authentication
from src.blocklist import BLOCKLIST
from src.utils.rbac import restricted
from src.controllers.user import Admin

blp = Blueprint("Admin", __name__, description="Operation performed via admin")


@blp.route('/admin/users')
class ListUsers(MethodView):
    @restricted('admin')
    @jwt_required()
    def get(self):
        admin_obj = Admin()
        return admin_obj.get_users()
