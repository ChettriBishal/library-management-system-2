from flask.views import MethodView
from flask_smorest import Blueprint, abort

blp = Blueprint("Authentication", __name__, url_prefix="/", description="Login operation")


# @blp.route("/login")
# class Login(MethodView):
#     def post(self):
#         return {"message": "Logged in"}


@blp.route("/signup")
class SignUp(MethodView):
    def post(self):
        return {"message": "Signed up"}
