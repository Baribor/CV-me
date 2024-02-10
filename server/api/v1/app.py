#!/usr/bin/python3
""" Flask Application """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask import make_response,jsonify
from api.v1.views import app_views


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cv_me_local:cv_me_pwd@localhost:5432/cv_me_local'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Register blueprints
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
