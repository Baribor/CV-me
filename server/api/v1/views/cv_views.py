#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response,current_app
from service.cv_service import CvService


@app_views.route("/cv", methods=['POST'])
def create_cv():
    """ Create a new user"""
    return jsonify({'error': 'Failed to create user'}), 500

@app_views.route('/cv/<int:user_id>', methods=['GET'])
def get_cv(cv_id):
    """Get CV"""
    cv = CvService.get_cv(user_id)
    if cv:
        return jsonify(cv), 200
    else:
        return jsonify({"error": "CV not found"}), 404

@app_views.route('/cv/<int:user_id>', methods=['DELETE'])
def delete_cv(cv_id):
    """Delete CV"""
    if CvService.delete_cv(user_id):
        return jsonify({"message": "CV deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete CV"}), 400
