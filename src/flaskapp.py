from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from src.routes.user_router import blp as LoginRouter
from src.routes.books_routes import blp as BookRoute
from src.routes.admin_routes import blp as AdminRoute
from src.routes.librarian_routes import blp as LibrarianRoute
from src.routes.visitor_routes import blp as VisitorRoute

from src.blocklist import BLOCKLIST

app = Flask(__name__)
app.app_context().push()

app.config["API_TITLE"] = "LMS API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config[
    "OPENAPI_SWAGGER_UI_URL"
] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["PROPAGATE_EXCEPTIONS"] = True

api = Api(app)
app.config["JWT_SECRET_KEY"] = "235911244572190182537651959146582626518"
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ),
        401,
    )


@jwt.needs_fresh_token_loader
def token_not_fresh_callback(jwt_header, jwt_payload):
    return (
        jsonify(
            {
                "description": "The token is not fresh.",
                "error": "fresh_token_required",
            }
        ),
        401,
    )


## check this
@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    if identity == 'admin':
        return {"is_admin": True}
    return {"is_admin": False}


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "The token has expired.", "error": "token_expired"}),
        401,
    )


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed.", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "description": "Request does not contain an access token.",
                "error": "authorization_required",
            }
        ),
        401,
    )


api.register_blueprint(LoginRouter)
api.register_blueprint(BookRoute)
api.register_blueprint(AdminRoute)
api.register_blueprint(LibrarianRoute)
api.register_blueprint(VisitorRoute)

app.run(debug=True, port=5000)
