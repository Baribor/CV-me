from flask import Blueprint, make_response


user_route = Blueprint("user", __name__)


@user_route.get("/")
def profile():
    return make_response({
        "message": "User profile retrieved successfully"
    })
