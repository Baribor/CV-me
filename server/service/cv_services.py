#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CVServices:
    @staticmethod
    def add_cv(cv_data):
        from models import CV  
        cv = CV(**cv_data)
        db.session.add(cv)
        db.session.commit()
        return cv

    @staticmethod
    def update_cv(cv_instance, new_data):
        cv_instance.update_data(new_data)
        db.session.commit()
        return cv_instance

    @staticmethod
    def delete_cv(cv_instance):
        db.session.delete(cv_instance)
        db.session.commit()

