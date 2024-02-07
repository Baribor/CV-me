#!/usr/bin/python3
""" Flask Application """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cv_me_local:cv_me_pwd@localhost:5432/cv_me_local'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import API views
from api.v1.views.users_views import user_bp
from api.v1.views.cv_views import cv_bp

# Register blueprints
app.register_blueprint(user_bp, url_prefix='/api/v1/users')
app.register_blueprint(cv_bp, url_prefix='/api/v1/cvs')
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
