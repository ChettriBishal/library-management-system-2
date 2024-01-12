from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256

from src.schemas import UserSchema
from src.controllers.authentication import Authentication

blp = Blueprint("Users", "users", description="Operation on users")


@blp.route('/login')
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
        if auth.login():
            return {"message": "user logged in successfully"}, 200
        abort(404, message="User not found")


@blp.route('/signup')
class UserSignUp(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        auth = Authentication(user_data['username'],user_data['password'], user_data['role'])
        if auth.signup():
            return {"message": f"{user_data['username']} signed up"}
        return {"message": "error"}
