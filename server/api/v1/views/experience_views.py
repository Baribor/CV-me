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

@experience_views.route('/<cv_id>/experience/<experience_id>', methods=['GET'])
def get_experience(cv_id, experience_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    experience = ExperienceService.get_experience(experience_id)
    if not experience:
        return jsonify({'message': 'No education found'}), 404
    return jsonify({'data': experience})

@experience_views.route('/<cv_id>/experience/<experience_id>', methods=['PUT'])
def edit_experience(cv_id, experience_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404

    payload = request.get_json()

    new_data ={
            'company': payload.get('company'),
            'position': payload.get('company'),
            'startDate': payload.get('startDate'),
            'endDate': payload.get('endDate')
    }

    updated_experience = ExperienceService.edit_experience(experience_id, new_data)
    if not updated_experience:
        return jsonify({'message': 'No experience found'}), 404

    return jsonify({'message': 'Experience updated successfully', 'data': updated_experience.to_dict()})


@experience_views.route('/<cv_id>/experience/<eperience_id>', methods=['DELETE'])
def delete_experience(cv_id, experience_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    deleted = ExperienceService.delete_experience(experience_id)
    if not deleted:
        return jsonify({'message': 'No education found'}), 404
    return jsonify({'message': 'Experience deleted successfully'}), 200



