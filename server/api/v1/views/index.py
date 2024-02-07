#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify,Blueprint
from flask import make_response


user_bp = Blueprint('users', __name__)
cv_bp = Blueprint('cv', __name__)


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def user_status():
    """ Status of users"""
    response_data = {"status": "OK"}
    response = make_response(jsonify(response_data), 200)
    return response

@app_views.route('/users/profile', methods=['GET'])
def view_profile():
    """ Get user data"""
    user = get_user_somehow()
    profile_data = UserService.view_profile(user)
    return jsonify(profile_data), 200
