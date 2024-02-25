from flask import Blueprint, g, jsonify, request
from api.v1.middlewares.authMiddleware import AuthMiddleware
from service.user_service import UserService
from service.cv_service import CVService
from service.project_service import ProjectService

project_views = Blueprint("project_views", __name__, url_prefix='/cv')


@project_views.route('/<cv_id>/project', methods=['POST'])
def create_project(cv_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    payload = request.get_json()
    print(payload)
    if not cv:
        return jsonify({'message': 'no cv found'}), 404
    project = ProjectService.create_project(**payload, cv_id=cv_id)
    return jsonify({'message': 'Project added successfully', 'data': project.to_dict()}), 201
