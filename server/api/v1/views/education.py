#!/usr/bin/python3
""" Flask routes for Project object related URI subpaths using the
app_views Blueprint.
"""
from . import app_views
from flask import jsonify, request
from models.education import Education
from models.base import Session
from datetime import datetime

@app_views.route("/education", methods=['POST'])
def create_education():
    """ Create a new Project"""
    education_data = request.json

    # Create a new object
    new_education = Education(
        institution=education_data.get('institution'),
        degree=education_data.get('degree'),
        startDate=datetime.strptime(education_data.get('startDate'), '%Y-%m-%d'),
        endDate=datetime.strptime(education_data.get('endDate'), '%Y-%m-%d'),
        cv_id=education_data.get('cv_id')
    )

    session = Session()
    session.add(new_education)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'Education created successfully'}), 201

@app_views.route("/education/<edu_id>", methods=['GET'])
def get_education(edu_id):
    session = Session()
    education = session.query(Education).filter_by(id=edu_id).first()
    if education:
        return jsonify(education.to_dict())
    else:
        return jsonify({'error': 'Education not found'}), 404

@app_views.route("/education/<edu_id>", methods=['PUT'])
def edit_education(edu_id):
    education_data = request.get_json()
    session = Session()
    education = session.query(Education).filter_by(id=edu_id).first()
    if education:
        for key, value in education_data.items():
            setattr(education, key, value)
        session.commit()
        return jsonify(education.to_dict()), 200
    else:
        return jsonify({'error': 'Education not found'}), 404

@app_views.route("/education/<edu_id>", methods=['DELETE'])
def delete_education(edu_id):
    session = Session()
    education = session.query(Education).filter_by(id=edu_id).first()
    if education:
        session.delete(education)
        session.commit()
        return jsonify({'message': 'Education deleted successfully'}), 200
    else:
        return jsonify({'error': 'Education not found'}), 404

