#!/usr/bin/python3
from flask import Blueprint, jsonify
from Service.user_service import UserService


user_bp = Blueprint('users', __name__)

# Define routes within the Blueprint

from flask import jsonify

@app_views.route('/users/new_user/<user_data>', methods=['POST'])
def create_new_user(user_data):
    """ Create a new user"""
    new_user = UserService.create_user(user_data)
    if new_user:
        return jsonify(new_user), 201
    else:
        return jsonify({'error': 'Failed to create user'}), 500 


@app_views.route('/users/profile/<int:user_id>', methods=['GET'])
def get_user_profile(user_id):
    """ Get user data"""
    profile_data = UserService.view_profile(user_id)
    if profile_data:
        return jsonify(profile_data), 200
    else:
        return jsonify({'error': 'User not found'}), 404
