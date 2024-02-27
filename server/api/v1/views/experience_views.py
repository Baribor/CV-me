from flask import Blueprint, g, jsonify, request
from api.v1.middlewares.authMiddleware import AuthMiddleware
from service.user_service import UserService
from service.cv_service import CVService
from service.experience_service import ExperienceService

experience_views = Blueprint("experiencie_views", __name__, url_prefix='/cv')


@experience_views.route('/<cv_id>/experience', methods=['POST'])
def create_experience(cv_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    payload = request.get_json()
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    experience = ExperienceService.create_experience(**payload, cv_id=cv_id)
    return jsonify({'message': 'Experience added successfully', 'data': experience.to_dict()}), 201

