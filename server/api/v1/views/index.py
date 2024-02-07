#!/usr/bin/python3
from flask import Blueprint, jsonify

# Create a Blueprint instance
app_views = Blueprint('app_views', __name__)


@app_views.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to CV-me API'})

from .user_views import user_bp
from .cv_views import cv_bp

# Register blueprints for other views
app_views.register_blueprint(user_bp)
app_views.register_blueprint(cv_bp)

