#!/usr/bin/python3

from api.v1.views import app_views,Blueprint
from flask import Flask, jsonify, abort, request
from service.user_service import UserService
from models.user import User


user_bp = Blueprint('users', __name__)




@app_views.route('/api/v1/users', methods= ['GET'])
def users():
    """ Status of users"""
    response_data = {"status": "OK"}    
    response = make_response(jsonify(response_data), 200)
    return response

@app_views.route('/api/v1/new_user/<user_data>', methods=['POST'])
def new_user(user_data):
    """ Create a new user"""
    new_user = UserService.create_user(user_data)
    if new_user:
        return jsonify(new_user), 201
    else:
        return jsonify({'error': 'Failed to create user'}), 500 


@app_views.route('/api/v1/user_profile/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    """ Get user data"""
    profile_data = UserService.view_profile(user_id)
    if profile_data:
        return jsonify(profile_data), 200
    else:
        return jsonify({'error': 'User not found'}), 404
