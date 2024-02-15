#!/usr/bin/python3
""" Flask routes for User object related URI subpaths using the
app_views Blueprint.
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response,current_app
from service.cv_service import CVService
from models.cv import CV

@app_views.route("/cv", methods=['POST'])
def create_cv():
    """ Create a new CV"""
    cv_data = request.get_json()
    title = cv_data.get('title')
    user_id = cv_data.get('user_id')

    if not title or not user_id:
        return jsonify({'error': 'Title and user ID are required'}), 400

    try:
        new_cv = CV(
            cv_id=cv_id,
            title=title,
            user_id=user_id,
            createdAt=datetime.utcnow(),
            UpdateddAt=datetime.utcnow()
        )
        session = Session()
        session.add(new_cv)
        session.commit()

        cv_dict = new_cv.to_dict()
        return jsonify(cv_dict), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_views.route("/cv/<int:user_id>", methods=['GET'])
def cv(user_id):
    cv_data = CVService.get_cv(user_id)
    if cv_data:
        cv_dict = cv_data.to_dict()
        return jsonify(cv_dict), 200
    else:
        return jsonify({'error': 'CV not found'}), 404

@app_views.route("/cv/<int:user_id>", methods=['PUT'])
def editcv(user_id):
    cv_data = request.get_json()
    edited_cv = CVService.edit_cv(user_id, cv_data)
    if edited_cv:
        edited_dict = edited_cv.todict()
        return jsonify(edited_cv), 200
    else:
        return jsonify({'error': 'CV not found'}), 404

@app_views.route("/cv/<int:user_id>", methods=['DELETE'])
def deletecv(user_id):
    deleted = CVService.delete_cv(user_id)
    if deleted:
        return jsonify({'message': 'CV deleted successfully'}), 200
    else:
        return jsonify({'error': 'CV not found'}), 404
