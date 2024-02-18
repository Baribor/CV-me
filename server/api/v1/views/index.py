#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify,Blueprint
from flask import make_response

index_bp = Blueprint('index', __name__)
cv_bp = Blueprint('cv', __name__)


@app_views.route('/')
def index():
    """ Status of users"""
    response_data = {"status": "OK"}
    response = make_response(jsonify(response_data), 200)
    return response

@app_views.route('/api/v1/users', methods= ['GET'])
def users():
    """ Status of users"""
    response_data = {"status": "OK"}
    response = make_response(jsonify(response_data), 200)
    return response
