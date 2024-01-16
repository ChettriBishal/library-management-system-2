from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from src.schemas import UserSchema
from src.controllers.authentication import Authentication
from src.blocklist import BLOCKLIST

blp = Blueprint("Users", __name__, description="Operation on users")


@blp.route('/login')
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
        logged_in = auth.login()
        if logged_in:
            access_token = create_access_token(identity=logged_in[0], fresh=True, additional_claims={"role": user_data['role']})
            refresh_token = create_refresh_token(identity=logged_in[0], additional_claims={"role": user_data['role']})
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        abort(404, message="User not found")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)  # it requires a refresh token
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)  # adding the previous token into blocklist while generating a new refresh token
        return {"access_token": new_token}


@blp.route('/signup')
class UserSignUp(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
        signed_up = auth.signup()
        if signed_up:
            return {"message": f"{user_data['username']} signed up, uuid {signed_up}"}
        return {"message": "error"}


@blp.route('/logout')
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}

# @blp.route('/admin/users')
# class AdminGetUsers(MethodView):
#     jwt = get_jwt()
#     if not jwt.get("is_admin"):
#         abort(401, message="Admin privilege required")

# def get(self):
#     return {"users": [1, 2, 3, 4]}
