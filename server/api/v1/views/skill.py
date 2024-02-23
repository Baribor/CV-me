#!/usr/bin/python3
""" Flask routes for Skill object related URI subpaths using the
app_views Blueprint.
"""
from . import app_views
from flask import jsonify, request
from models.skill import Skill
from models.base import Session
from datetime import datetime

@app_views.route("/skill", methods=['POST'])
def create_skill():
    """ Create a new skill"""
    skill_data = request.json

    # Create a new object
    new_skill = Skill(
        skillName=skill_data.get('skillName'),
        proficiency=skill_data.get('proficiency'),
        cv_id= skill_data.get('cv_id')
    )

    session = Session()
    session.add(new_skill)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'Skill created successfully'}), 201

@app_views.route("/skill/<skill_id>", methods=['GET'])
def get_skill(skill_id):
    session = Session()
    skill = session.query(Skill).filter_by(id=skill_id).first()
    if skill:
        return jsonify(skill.to_dict())
    else:
        return jsonify({'error': 'Skill not found'}), 404

@app_views.route("/skill/<skill_id>", methods=['PUT'])
def edit_skill(skill_id):
    skill_data = request.get_json()
    session = Session()
    skill = session.query(Skill).filter_by(id=skill_id).first()
    if skill:
        for key, value in skill_data.items():
            setattr(skill, key, value)
        session.commit()
        return jsonify(skill.to_dict()), 200
    else:
        return jsonify({'error': 'Skill not found'}), 404

@app_views.route("/skill/<skill_id>", methods=['DELETE'])
def delete_skill(skill_id):
    session = Session()
    skill = session.query(Skill).filter_by(id=skill_id).first()
    if skill:
        session.delete(skill)
        session.commit()
        return jsonify({'message': 'Skill deleted successfully'}), 200
    else:
        return jsonify({'error': 'Skill not found'}), 404

