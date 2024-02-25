#!/usr/bin/python3
""" Flask Application """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask import make_response,jsonify
from .views import app_views
from models.base import Session
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import dotenv
dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
bcrypt = Bcrypt(app)
# migrate = Migrate(app, db)

# Register blueprints
cors = CORS(app)

@app.route('/api/v1/status', methods= ['GET'])
def status():
    """ Status of users"""
    response_data = {"status": "OK"}
    response = make_response(jsonify(response_data), 200)
    return response

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.errorhandler(401)
def unauthorized(error):
    """401 - AUTHORIZED ACCESS
    """
    return make_response(jsonify({'message': "Unauthorized access"}), 401)


print(app.url_map)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
                         
