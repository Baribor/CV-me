#!/usr/bin/python3
""" Flask routes for SmartURL object related URI subpaths using the
app_views Blueprint.
"""
from . import app_views
from flask import jsonify, request
from models.smarturl import SmartUrl
from models.base import Session
from datetime import datetime

@app_views.route("/smarturl", methods=['POST'])
def create_smarturl():
    """ Create a new smarturl"""
    smarturl_data = request.json

    # Create a new object
    new_smarturl = SmartURL(
        urlName=smarturl_data.get('urlName'),
        url=smarturl_data.get('url'),
        viewedAt=smarturl_data.get('viewedAt')
    )

    session = Session()
    session.add(new_smarturl)
    session.commit()

    # Return a response indicating success
    return jsonify({'message': 'SmartURL created successfully'}), 201

@app_views.route("/smarturl/<smarturl_id>", methods=['GET'])
def get_smarturl(smarturl_id):
    session = Session()
    smarturl = session.query(SmartURL).filter_by(id=smarturl_id).first()
    if smarturl:
        return jsonify(smarturl.to_dict())
    else:
        return jsonify({'error': 'SmartURL not found'}), 404

@app_views.route("/smarturl/<smarturl_id>", methods=['PUT'])
def edit_smarturl(smarturl_id):
    smarturl_data = request.get_json()
    session = Session()
    smarturl = session.query(SmartURL).filter_by(id=smarturl_id).first()
    if smarturl:
        for key, value in smarturl_data.items():
            setattr(smarturl, key, value)
        session.commit()
        return jsonify(smarturl.to_dict()), 200
    else:
        return jsonify({'error': 'SmartURL not found'}), 404

@app_views.route("/smarturl/<smarturl_id>", methods=['DELETE'])
def delete_smarturl(smarturl_id):
    session = Session()
    smarturl = session.query(SmartURL).filter_by(id=smarturl_id).first()
    if smarturl:
        session.delete(smarturl)
        session.commit()
        return jsonify({'message': 'SmartURL deleted successfully'}), 200
    else:
        return jsonify({'error': 'SmartURL not found'}), 404

