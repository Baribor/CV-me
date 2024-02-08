#!/usr/bin/python3
from flask import Blueprint, jsonify
from service.user_service import UserService
from api.v1.views import app_views


user_bp = Blueprint('users', __name__)

@app_views.route('/new_user', methods=['POST'])
def new_user(user_data):
    """ Create a new user"""
    new_user = UserService.create_user(user_data)
    if new_user:
        return jsonify(new_user), 201
    else:
        return jsonify({'error': 'Failed to create user'}), 500 


@app_views.route('/user_profile/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    """ Get user data"""
    profile_data = UserService.view_profile(user_id)
    if profile_data:
        return jsonify(profile_data), 200
    else:
        return jsonify({'error': 'User not found'}), 404
