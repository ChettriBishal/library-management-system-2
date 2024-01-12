from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from src.routes.auth_router import blp as AuthRouter
from src.routes.user_router import blp as LoginRouter

app = Flask(__name__)
app.config["API_TITLE"] = "Stores REST API"
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

api.register_blueprint(LoginRouter)

app.run(debug=True, port=5000)
