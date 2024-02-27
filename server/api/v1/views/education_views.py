from flask import Blueprint, g, jsonify, request
from api.v1.middlewares.authMiddleware import AuthMiddleware
from service.user_service import UserService
from service.cv_service import CVService
from service.education_service import EducationService  

education_views = Blueprint("education_views", __name__, url_prefix='/cv')


@education_views.route('/<cv_id>/education', methods=['POST'])
def create_education(cv_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    payload = request.get_json()
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    education = EducationService.create_education(**payload, cv_id=cv_id)
    return jsonify({'message': 'Education added successfully', 'data': education.to_dict()}), 201

@education_views.route('/<cv_id>/education/<education_id>', methods=['GET'])
def get_education(cv_id, education_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    education = EducationService.get_education(education_id)
    if not education:
        return jsonify({'message': 'No education found'}), 404
    return jsonify({'data': education.to_dict()})

@education_views.route('/<cv_id>/education/<education_id>', methods=['PUT'])
def edit_education(cv_id, education_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    payload = request.get_json()
    updated_education = EducationService.edit_education(education_id, **payload)
    if not updated_education:
        return jsonify({'message': 'No education found'}), 404
    return jsonify({'message': 'Education updated successfully', 'data': updated_education.to_dict()})

@education_views.route('/<cv_id>/education/<education_id>', methods=['DELETE'])
def delete_education(cv_id, education_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    deleted = EducationService.delete_education(education_id)  
    if not deleted:
        return jsonify({'message': 'No education found'}), 404
    return jsonify({'message': 'Education deleted successfully'}), 200

