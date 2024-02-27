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
    return jsonify({'message': 'Skill added successfully', 'data': skill.to_dict()}), 201

