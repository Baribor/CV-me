#!/usr/bin/python3
from flask import Blueprint, jsonify


user_bp = Blueprint('users', __name__)

# Define routes within the Blueprint
@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users=[user.to_dict() for user in users])

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(user=user.to_dict())


