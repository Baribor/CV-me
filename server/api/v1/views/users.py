#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response,current_app
from service.user_service import UserService
from models.user import User

@app_views.route("/users", methods=['POST'])
def create_user():
    """ Create a new user"""
    user_data = request.get_json()
    sex = user_data.get('sex')


    if sex is None:
        return jsonify({'error': 'Sex field is missing'}), 400

    new_user = UserService.create_user(
        user_data.get('username'),
        user_data.get('first_name'),
        user_data.get('last_name'),
        user_data.get('email'),
        user_data.get('password_hash'),
        user_data.get('age'),
        sex
    )
    if new_user:
        user_dict = new_user.to_dict()
        return jsonify(user_dict), 201
    else:
        return jsonify({'error': 'Failed to create user'}), 500

@app_views.route("/profile/<user_id>", methods=['GET'])
def userprofile(user_id):
    """ view profile"""
    user_prof = UserService.view_profile(user_id)
    if user_prof:
        user_prof_dict = new_prof.to_dict()
        return jsonify(user_prof_dict), 200
    else:
        return jsonify({'error': 'User profile not found'}), 404

@app_views.route("/editprofile/<int:user_id>", methods=['PUT'])
def edit_profile(user_id):
    """ edit user profile """
    new_data = request.get_json()
    user_prof = UserService.edit_profile(user_id, new_data)
    if user_prof:
        user_prof_dict = user_prof.to_dict()
        return jsonify(user_prof_dict), 200
    else:
        return jsonify({'error': 'User profile not found'}), 404

@app_views.route("/users/<int:user_id>", methods=['DELETE'])
def delete_profile(user_id):
    """ Delete user profile """
    if UserService.delete_user(user_id):
        return jsonify({'message': 'User profile deleted successfully'}), 200
    else:
        return jsonify({'error': 'User profile not found'}), 404

