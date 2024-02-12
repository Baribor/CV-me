#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response,current_app
from service.cv_service import CvService


@app_views.route("/cv", methods=['POST'])
def create_cv(cv_data):
    """ Create a new cv"""
     title = cv_data.get('title')
    user_id = cv_data.get('user_id')

    # Check if title and user_id are provided
    if not title or not user_id:
        return jsonify({'error': 'Title and user ID are required'}), 400

    # Create a new CV instance
    new_cv = CV(
        title=title,
        user_id=user_id,
        createdAt=datetime.utcnow(),  
        UpdateddAt=datetime.utcnow()
        

@app_views.route('/cv/<int:cv_id>', methods=['GET'])
def get_cv(cv_id):
    """Get CV"""
    cv = CvService.get_cv(cv_id)
    if cv:
        return jsonify(cv), 200
    else:
        return jsonify({"error": "CV not found"}), 404

@app_views.route('/cv/<int:cv_id>', methods=['DELETE'])
def delete_cv(cv_id):
    """Delete CV"""
    if CvService.delete_cv(cv_id):
        return jsonify({"message": "CV deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete CV"}), 400
