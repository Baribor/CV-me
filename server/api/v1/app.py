#!/usr/bin/python3
""" Flask Application """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cv_me_local:cv_me_local@localhost/cv_me_pwd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models.user import User
from models.cv import CV
from models.project import Project
from models.skill import Skill
from models.education import Education
from models.experience import Experience

# Import API views
from api.v1.views.users_views import user_bp
from api.v1.views.cv_views import cv_bp

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api/v1/users')
app.register_blueprint(cv_bp, url_prefix='/api/v1/cvs')

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=3000 debug=True)





































