#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from .auth import auth_views
from .cv_views import cv_views
from .project_views import project_views

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
app_views.register_blueprint(auth_views)
app_views.register_blueprint(cv_views)
app_views.register_blueprint(project_views)


from .users import *
from .project import *
from .education import *
from .experience import *
from .smarturl import *
