import sys
import os
import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import User
from models import CV
from models import Project

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cv_me_local:cv_me_local@localhost/cv_me_pwd'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Initialize the Flask application context
        self.app.app_context().push()

        # Create the SQLAlchemy instance after initializing the app context
        self.db = SQLAlchemy(self.app)

        # Create the tables
        with self.app.app_context():
            self.db.create_all()

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_user_model(self):
        with self.app.app_context():
            user = User(username='test_user', email='test@example.com')
            self.db.session.add(user)
            self.db.session.commit()

            retrieved_user = User.query.filter_by(username='test_user').first()
            self.assertIsNotNone(retrieved_user)
            self.assertEqual(retrieved_user.email, 'test@example.com')

    def test_cv_model(self):
        with self.app.app_context():
            user = User(username='test_user', email='test@example.com')
            cv = CV(title='Test CV', user=user)
            self.db.session.add(user)
            self.db.session.add(cv)
            self.db.session.commit()

            retrieved_cv = CV.query.filter_by(title='Test CV').first()
            self.assertIsNotNone(retrieved_cv)
            self.assertEqual(retrieved_cv.user.username, 'test_user')

    def test_project_model(self):
        with self.app.app_context():
            user = User(username='test_user', email='test@example.com')
            cv = CV(title='Test CV', user=user)
            project = Project(project_name='Test Project', cv=cv)
            self.db.session.add(user)
            self.db.session.add(cv)
            self.db.session.add(project)
            self.db.session.commit()

            retrieved_project = Project.query.filter_by(project_name='Test Project').first()
            self.assertIsNotNone(retrieved_project)
            self.assertEqual(retrieved_project.cv.title, 'Test CV')

if __name__ == '__main__':
    unittest.main()
