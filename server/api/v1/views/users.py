#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from ..views import app_views
from flask import Flask, jsonify, abort, request, make_response, current_app, g
from ....service.user_service import UserService
from ....models.user import User
from ....models.base import Session
from ..middlewares.authMiddleware import require_authentication


@app_views.route("/profile", methods=['GET'])
@require_authentication
def userprofile():
    """ view profile"""

    user_prof = UserService.view_profile(g.user['sub'])
    if user_prof:
        user_prof_dict = {
            'id': user_prof.id,
            'username': user_prof.username,
            'first_name': user_prof.first_name,
            'last_name': user_prof.last_name,
            'email': user_prof.email,
            'age': user_prof.age,
            'sex': user_prof.sex,
        }
        return jsonify({'message': 'profile retrieve successfully', 'data': user_prof_dict}), 200
    else:
        return jsonify({'error': 'User profile not found'}), 404




@app_views.route("/users/<user_id>", methods=['PUT'])
def edit_profile(user_id):
    """ edit user profile """
    new_data = request.get_json()
    user_prof = UserService.edit_profile(user_id, new_data)
    if user_prof:
        user_prof_dict = user_prof.to_dict()
        return jsonify(user_prof_dict), 200
    else:
        return jsonify({'error': 'edit not succesful'}), 404

@app_views.route("/users/<user_id>", methods=['DELETE'])
def delete_profile(user_id):
    """ Delete user profile """
    if UserService.delete_user(user_id):
        return jsonify({'message': 'User profile deleted successfully'}), 200
    else:
        return jsonify({'error': 'User profile not deleted'}), 404

