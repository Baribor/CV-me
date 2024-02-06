#!/usr/bin/python3
from flask import Blueprint, jsonify
""" view for user cv's """
cv_bp = Blueprint('cv', __name__)


@cv_bp.route('/cv', methods=['GET'])
def get_cv():
     return jsonify({"status": "CV"})
