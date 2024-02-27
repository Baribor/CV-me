from flask import Blueprint, g, jsonify, request
from api.v1.middlewares.authMiddleware import AuthMiddleware
from service.user_service import UserService
from service.cv_service import CVService
from service.project_service import ProjectService
from sqlalchemy import and_
from uuid import UUID


project_views = Blueprint("project_views", __name__, url_prefix='/cv')

@project_views.route('/<cv_id>/project', methods=['POST'])
def create_project(cv_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    payload = request.get_json()
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    project = ProjectService.create_project(**payload, cv_id=cv_id)
    return jsonify({'message': 'Project added successfully', 'data': project.to_dict()}), 201


@project_views.route('/<cv_id>/project/<project_id>', methods=['GET'])
def get_project(cv_id,project_id):
    try:
        cv_uuid = UUID(cv_id)
        project_uuid = UUID(project_id)
    except ValueError:
        return jsonify({'message': 'Invalid UUID format'}), 400

    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    ProjectService.find_first(cv_id=cv_id, id=project_id)
    if not project:
        return jsonify({'message': 'No project found'}), 404
    return jsonify({'data': project})


@project_views.route('/<cv_id>/project/<project_id>', methods=['PUT'])
def edit_project(cv_id, project_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    payload = request.get_json()
    updated_project = ProjectService.edit_project(project_id, **payload)
    if not updated_project:
        return jsonify({'message': 'No project found'}), 404
    return jsonify({'message': 'Project updated successfully', 'data': updated_project.to_dict()})


@project_views.route('/<cv_id>/project/<project_id>', methods=['DELETE'])
def delete_project(cv_id, project_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    deleted = ProjectService.delete_project(project_id)
    if not deleted:
        return jsonify({'message': 'No project found'}), 404
    return jsonify({'message': 'Project deleted successfully'}), 200

