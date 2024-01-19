import os
from flask.views import MethodView
import requests
from flask_smorest import Blueprint, abort
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt

from src.schemas import UserSchema, UserRegisterSchema
from src.controllers.authentication import Authentication
from src.blocklist import BLOCKLIST
from src.config.constants import authorization_bearer

blp = Blueprint("Users", __name__, description="Operation on users")


def send_simple_message(to, subject, body):
    domain = os.getenv("MAILGUN_DOMAIN")
    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", os.getenv("MAILGUN_API_KEY")),
        data={"from": f"Bishal Chettri <mailgun@{domain}>",
              "to": [to],
              "subject": subject,
              "text": body})


@blp.route('/login')
class UserLogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
        logged_in = auth.login()
        if logged_in:
            access_token = create_access_token(identity=logged_in[0], fresh=True,
                                               additional_claims={"role": user_data['role'],
                                                                  "username": user_data['username']})
            refresh_token = create_refresh_token(identity=logged_in[0], additional_claims={"role": user_data['role'],
                                                                                           "username": user_data[
                                                                                               'username']})
            return {"access_token": access_token, "refresh_token": refresh_token}, 200
        abort(404, message="User not found")


@blp.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required(refresh=True)  # it requires a refresh token
    @blp.doc(parameters=authorization_bearer)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)  # adding the previous token into blocklist while generating a new refresh token
        return {"access_token": new_token}


@blp.route('/signup')
class UserSignUp(MethodView):
    @blp.arguments(UserRegisterSchema)
    def post(self, user_data):
        try:
            auth = Authentication(user_data['username'], user_data['password'], user_data['role'])
            email = user_data['email']
            signed_up = auth.signup()
            if signed_up:
                send_simple_message(
                    to=email,
                    subject="Successfully signed up",
                    body=f"Hey {user_data['username']}! You have successfully signed up to the LMS."
                )
                return {"message": f"{user_data['username']} signed up, uuid {signed_up}"}
        except Exception as err:
            abort(400, message="Something went wrong")


@blp.route('/logout')
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Successfully logged out"}, 200
