#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response,current_app
from service.user_service import UserService


@app_views.route("/users", methods=['POST'])
def create_user():
    """ Create a new user"""
    user_data = request.get_json()
    current_app.logger.debug(f"Received JSON data: {user_data}")
    sex = user_data.get('sex')
    current_app.logger.debug(f"Extracted sex field: {sex}")


    if sex is None:
        return jsonify({'error': 'Sex field is missing'}), 400

    new_user = UserService.create_user(
        user_data.get('id'),
        user_data.get('username'),
        user_data.get('first_name'),
        user_data.get('last_name'),
        user_data.get('email'),
        user_data.get('password_hash'),
        user_data.get('age'),
        sex
    )
    if new_user:
        return jsonify(new_user), 201
    else:
        return jsonify({'error': 'Failed to create user'}), 500

@app_views.route("/profile/<user_id>", method=['POST']
def userprofile(user_id):
    """ view profile"""
    user_prof = UserServices.view_profile(user_id)


