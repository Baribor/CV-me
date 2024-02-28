from flask import Blueprint, g, jsonify, request
from api.v1.middlewares.authMiddleware import AuthMiddleware
from service.user_service import UserService
from service.cv_service import CVService
from service.skill_service import SkillService

skill_views = Blueprint("skill_views", __name__, url_prefix='/cv')


@skill_views.route('/<cv_id>/skill', methods=['POST'])
def create_skill(cv_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    payload = request.get_json()
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    skill = SkillService.create_skill(**payload, cv_id=cv_id)
    return jsonify({'message': 'Skill added successfully', 'data': skill.to_dict()}), 

@skill_views.route('/<cv_id>/skill/<skill_id>', methods=['GET'])
def get_skill(cv_id, skill_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    skill = SkillService.get_skill(skill_id)
    if not skill:
        return jsonify({'message': 'No skills found'}), 404
    return jsonify({'data': skill})


@skill_views.route('/<cv_id>/skill/<skill_id>', methods=['PUT'])
def edit_skill(cv_id, skill_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404

    payload = request.get_json()

    new_data ={
            'description': payload.get('description'),
            'proficiency': payload.get('proficiency')
    }

    updated_skill = SkillService.edit_skill(skill_id, new_data)
    if not updated_skill:
        return jsonify({'message': 'No experience found'}), 404

    return jsonify({'message': 'Skill updated successfully', 'data': updated_skill.to_dict()})


@skill_views.route('/<cv_id>/skill/<skill_id>', methods=['DELETE'])
def delete_skill(cv_id, skill_id):
    AuthMiddleware().authenticate()
    username = g.user['sub']
    user = UserService.view_profile(username)
    cv = CVService.find_first(user_id=user.id, id=cv_id)
    if not cv:
        return jsonify({'message': 'No CV found'}), 404
    deleted = SkillService.delete_skill(skill_id)
    if not deleted:
        return jsonify({'message': 'No skill found'}), 404
    return jsonify({'message': 'skill deleted successfully'}), 200
