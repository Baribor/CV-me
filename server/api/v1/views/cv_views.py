#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
cv_views Blueprint.
"""
from flask import Flask, jsonify, abort, request, make_response, current_app, Blueprint, g
from service.cv_service import CVService
from service.user_service import UserService
from models.cv import CV
import uuid
from datetime import datetime
from models.base import Session
from api.v1.middlewares.authMiddleware import AuthMiddleware

cv_views = Blueprint('cv_views', __name__, url_prefix="/cv")


@cv_views.route("/", methods=['POST'], )
def create_cv():
    """ Create a new CV"""
    AuthMiddleware().authenticate()
    username = g.user['sub']
    print(username)
    user = UserService.view_profile(username)
    print(user)
    cv_data = request.json
    session = Session()

    # Create a new CV object
    new_cv = CV(
        title=cv_data['title'],
        user_id=user.id,

        # createdAt=datetime.utcnow(),
        # UpdateddAt=datetime.utcnow()
    )

    session.add(new_cv)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'CV created successfully'}), 201


@cv_views.route("/<cv_id>", methods=['GET'])
def get_cv(cv_id):
    AuthMiddleware().authenticate()
    session = Session()
    user = UserService.view_profile(g.user['sub'])
    cv = session.query(CV).filter_by(id=cv_id, user_id=user.id).first()
    if cv:
        data = {
            **cv.to_dict(),
            'projects': [p.to_dict() for p in cv.projects],
            'educations': [e.to_dict() for e in cv.educations],
            'skills': [e.to_dict() for e in cv.skills],
            'experiences': [e.to_dict() for e in cv.experiences],
        }
        return jsonify({'message': 'CV rerieved', 'data': data})
    else:
        return jsonify({'error': 'CV not found'}), 404


@cv_views.route("/", methods=['GET'])
def get_all_cvs():
    AuthMiddleware().authenticate()
    session = Session()
    user = UserService.view_profile(g.user['sub'])
    cvs = session.query(CV).filter_by(user_id=user.id).all()
    if cvs:
        return jsonify([cv.to_dict() for cv in cvs])
    else:
        return jsonify({'error': 'CV not found'}), 404


@cv_views.route("/<cv_id>", methods=['PUT'])
def editcv(cv_id):
    AuthMiddleware().authenticate()
    cv_data = request.get_json()
    edited_cv = CVService.edit_cv(cv_id, new_data=cv_data)
    if edited_cv:
        edited_dict = edited_cv.to_dict()
        return jsonify(edited_cv), 200
    else:
        return jsonify({'error': 'CV not found'}), 404


@cv_views.route("/<user_id>", methods=['DELETE'])
def deletecv(user_id):
    AuthMiddleware().authenticate()
    deleted = CVService.delete_cv(user_id)
    if deleted:
        return jsonify({'message': 'CV deleted successfully'}), 200
    else:
        return jsonify({'error': 'CV not found'}), 404
