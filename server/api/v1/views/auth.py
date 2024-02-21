#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from flask import Flask, jsonify, abort, request, make_response, current_app
from service.user_service import UserService
from models.user import User
from models.base import Session
from flask import Blueprint

auth_views = Blueprint('app_views', __name__, url_prefix='/auth')


@auth_views.route("/signup", methods=['POST'])
def create_user():
    """ Create a new user"""
    user_data = request.get_json()
    user_in_db = Session().query(User).filter_by(
        username=user_data.get('username'), email=user_data.get('email')).first()

    if user_in_db:
        return jsonify({'message': 'User with email or username already exist'}), 401

    new_user = UserService.create_user(
        user_data.get('username'),
        user_data.get('first_name'),
        user_data.get('last_name'),
        user_data.get('email'),
      	user_data.get('password'),
    )

    if new_user:
        # Check if the user exists in the database
        user_in_db = Session().query(User).filter_by(
            username=user_data.get('username')).first()
        return jsonify({'message': 'Sign up successful', 'data': user_in_db.to_dict()}), 201
    else:
        return jsonify({'message': 'Server error'}), 500


@auth_views.route("/login", methods=['POST'])
def login():
    "Login a user"
    body = request.get_json()
    user = Session().query(User).filter_by(email=body.get('email')).first()
    if not user:
        return jsonify({"message": "Incorrect email or password"}), 401
    if user.check_password(body.get('password')):
        data = user.to_dict()
        data['token'] = user.encode_auth_token()
        return jsonify({"message": "Login successful", 'data': data}), 200
    else:
        return jsonify({"message": "Incorrect email or password"}), 401
