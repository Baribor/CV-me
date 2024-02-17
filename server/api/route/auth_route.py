from flask import Blueprint, make_response

auth_route = Blueprint("auth", __name__)


@auth_route.post("/login")
def login():
    return make_response({
        "message": "Logging in"
    })


@auth_route.post("/signup")
def signup():
    return make_response({
        "message": "signing up"
    })


@auth_route.post("/reset_password")
def reset_password():
    return make_response({
        "message": "resetting password"
    })
