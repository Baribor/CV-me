#!/usr/bin/python3
from flask import Blueprint, jsonify
from service.cv_service import CVService

cv_bp = Blueprint('cv', __name__)

@cv_bp.route('/cv/<int:user_id>', methods=['POST'])
def create_cv(user_id):
    """Create CV"""
    cv_data = request.json  # Assuming JSON data is sent in the request
    cv = CVService.create_cv(user_id, cv_data)
    if cv:
        return jsonify({"message": "CV created successfully"}), 201
    else:
        return jsonify({"error": "Failed to create CV"}), 400

@cv_bp.route('/cv/<int:user_id>', methods=['GET'])
def get_cv(cv_id):
    """Get CV"""
    cv = CVService.get_cv(user_id)
    if cv:
        return jsonify(cv), 200
    else:
        return jsonify({"error": "CV not found"}), 404

@cv_bp.route('/cv/<int:user_id>', methods=['DELETE'])
def delete_cv(cv_id):
    """Delete CV"""
    if CVService.delete_cv(user_id):
        return jsonify({"message": "CV deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete CV"}), 400
