#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from flask import Flask, jsonify, abort, request, make_response,current_app, g
from service.cv_service import CVService
from models.cv import CV
import uuid
from datetime import datetime
from models.base import Session
from models.user import User
from flask import Blueprint
from api.v1.middlewares.authMiddleware import require_authentication

cv_views = Blueprint('api_v1_blueprint', __name__, url_prefix='/api/v1')


@cv_views.route("/create", methods=['POST'])
@require_authentication
def create_cv():
    """ Create a new CV"""
    cv_data = request.json
    session = Session()

    # Create a new CV object
    new_cv = CV(
        title=cv_data['title'],
        user_id=cv_data['user_id'],
        createdAt=datetime.utcnow(),
        UpdateddAt=datetime.utcnow()
    )

    session.add(new_cv)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'CV created successfully'}), 201


@cv_views.route("/cv/", methods=['GET'])
def cv():
    session = Session()
    cv = session.query(CV).filter_by(id=cv_id).first()
    if cv:
        return jsonify(cv.to_dict())
    else:
        return jsonify({'error': 'CV not found'}), 404



@cv_views.route("/edit/<cv_id>", methods=['PUT'])
def edit(cv_id):
    cv_data = request.get_json()
    edited_cv = CVService.edit_cv(cv_id, new_data=cv_data)
    if edited_cv:
        edited_dict = edited_cv.to_dict()
        return jsonify(edited_cv), 200
    else:
        return jsonify({'error': 'CV not found'}), 404

@cv_views.route("/delete/<cv_id>", methods=['DELETE'])
def deletecv(cv_id):
    deleted = CVService.delete_cv(cv_id)
    if deleted:
        return jsonify({'message': 'CV deleted successfully'}), 200
    else:
        return jsonify({'error': 'CV not found'}), 404
