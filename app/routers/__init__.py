from dotenv import load_dotenv

load_dotenv()
import os

from flask import Blueprint
from flask_restx import Api

# user management
from app.routers.user_management.login import user_login_namespace
from app.routers.user_management.signup import user_registration_namespace
from app.routers.user_management.forgotpassword import user_forgot_password_namespace

# from import sample
# from import sample
# from import sample


api_bp = Blueprint("api", __name__, url_prefix="/api/v1")
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

if os.getenv("DEVELOPMENT_MODE") == "local_development" or os.getenv("DEVELOPMENT_MODE") == "development":
    api = Api(
        api_bp, version="1.0", title="Flask-Sample-DEV",
        description="Rest api created in python using flask_restx  with all sample API i DEV",
        doc="/swagger",
        authorizations=authorizations,
        security='Bearer', url_scheme="https,http")
elif os.getenv("DEVELOPMENT_MODE") == "qa":
    api = Api(
        api_bp, version="1.0", title="Flask-Sample-QA",
        description="Rest api created in python using flask_restx  with all sample API i QA",
        doc="/swagger",
        authorizations=authorizations,
        security='Bearer')
else:
    api = Api(api_bp, doc="False")

# user management namespace
api.add_namespace(user_login_namespace, path="/usermanagement")
api.add_namespace(user_registration_namespace, path="/usermanagement")
api.add_namespace(user_forgot_password_namespace, path="/usermanagement")

# another namespace
# another namespace
# another namespace
# another namespace
# another namespace
# another namespace
