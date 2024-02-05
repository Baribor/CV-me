from flask import Blueprint, jsonify

# Create a Blueprint instance for users
cv_bp = Blueprint('cv', __name__)

# Define routes within the Blueprint
@cv_bp.route('/cv', methods=['GET'])
def get_cv():
     return jsonify({"status": "CV"})
