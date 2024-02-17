from flask import Blueprint, make_response
from .auth_route import auth_route
from .cv_route import cv_route
from .user_route import user_route

api_base = Blueprint("index", __name__)


@api_base.get("")
def index():
    return make_response({
        "message": "Welcome to cvME API!!"
    })


api_base.register_blueprint(auth_route, url_prefix="/auth")
api_base.register_blueprint(cv_route, url_prefix="/cv")
api_base.register_blueprint(user_route, url_prefix="/profile")
