#!/usr/bin/python3
""" Flask Application """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://cv_me_test@localhost:cv_me_test_pswd@localhost/cv_me_test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import models
from models.user import User
from models.cv import CV
from models.project import Project
from models.skill import Skill
from models.education import Education
from models.experience import Experience
from models.smart_url import SmartUrl

# Import API views
from api.v1.views.user_views import user_bp
from api.v1.views.cv_views import cv_bp

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api/v1/users')
app.register_blueprint(cv_bp, url_prefix='/api/v1/cvs')

if __name__ == '__main__':
    app.run(debug=True)





































