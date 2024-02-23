#!/usr/bin/python3
""" Flask routes for Experience object related URI subpaths using the
app_views Blueprint.
"""
from . import app_views
from flask import jsonify, request
from models.experience import Experience
from models.base import Session
from datetime import datetime

@app_views.route("/experience", methods=['POST'])
def create_experience():
    """ Create a new experience"""
    experience_data = request.json

    # Create a new object
    new_experience = Experience(
        company=experience_data.get('company'),
        position=experience_data.get('position'),
        startDate=datetime.strptime(experience_data.get('startDate'), '%Y-%m-%d'),
        endDate=datetime.strptime(experience_data.get('endDate'), '%Y-%m-%d')
    )

    session = Session()
    session.add(new_experience)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'Experience created successfully'}), 201

@app_views.route("/experience/<exp_id>", methods=['GET'])
def get_experience(exp_id):
    session = Session()
    experience = session.query(Experience).filter_by(id=exp_id).first()
    if experience:
        return jsonify(experience.to_dict())
    else:
        return jsonify({'error': 'Experience not found'}), 404

@app_views.route("/experience/<exp_id>", methods=['PUT'])
def edit_experience(exp_id):
    experience_data = request.get_json()
    session = Session()
    experience = session.query(Experience).filter_by(id=exp_id).first()
    if experience:
        for key, value in experience_data.items():
            setattr(experience, key, value)
        session.commit()
        return jsonify(experience.to_dict()), 200
    else:
        return jsonify({'error': 'Experience not found'}), 404

@app_views.route("/experience/<exp_id>", methods=['DELETE'])
def delete_experience(exp_id):
    session = Session()
    experience = session.query(Experience).filter_by(id=exp_id).first()
    if experience:
        session.delete(experience)
        session.commit()
        return jsonify({'message': 'Experience deleted successfully'}), 200
    else:
        return jsonify({'error': 'Experience not found'}), 404

