#!/usr/bin/python3
""" Index """

from api.v1.views import app_views
from flask import jsonify,Blueprint

user_bp = Blueprint('users', __name__)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def user_status():
    """ Status of users"""
    return jsonify({"status": "OK"})

