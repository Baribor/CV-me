#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from .auth import auth_views

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
app_views.register_blueprint(auth_views)

from .users import *
from .cv_views import *
from .users import *
from .project import *
from .education import *
from . import *
