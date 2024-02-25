#!/usr/bin/python3
""" Flask routes for Project object related URI subpaths using the
app_views Blueprint.
"""

from flask import jsonify, request,g
from models.project import Project
from models.base import Session
from models.user import User
from datetime import datetime
from flask import Blueprint
from api.v1.middlewares.authMiddleware import require_authentication


project_views = Blueprint('api_v1_blueprinit', __name__, url_prefix='/project')



@project_views.route("/", methods=['POST'])
@require_authentication
def create_project():
    
    """ Create a new Project"""
    project_data = request.json

    # Create a new object
    new_project = Project(
        projectName=project_data.get('projectName'),
        description=project_data.get('description'),
        startDate=datetime.strptime(project_data.get('startDate'), '%Y-%m-%d'),
        endDate=datetime.strptime(project_data.get('endDate'), '%Y-%m-%d'),
        cv_id=project_data.get('cv_id')
    )

    session = Session()
    session.add(new_project)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'Project created successfully'}), 201

@project_views.route("/getproject/<pj_id>", methods=['GET'])
def get_project(pj_id):
    session = Session()
    project = session.query(Project).filter_by(id=pj_id).first()
    if project:
        return jsonify(project.to_dict())
    else:
        return jsonify({'error': 'Project not found'}), 404

@project_views.route("/edit/<pj_id>", methods=['PUT'])
def edit_project(pj_id):
    project_data = request.get_json()
    session = Session()
    project = session.query(Project).filter_by(id=pj_id).first()
    if project:
        for key, value in project_data.items():
            setattr(project, key, value)
        session.commit()
        return jsonify(project.to_dict()), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

@project_views.route("/delete_project/<pj_id>", methods=['DELETE'])
def delete_project(pj_id):
    session = Session()
    project = session.query(Project).filter_by(id=pj_id).first()
    if project:
        session.delete(project)
        session.commit()
        return jsonify({'message': 'Project deleted successfully'}), 200
    else:
        return jsonify({'error': 'Project not found'}), 404

