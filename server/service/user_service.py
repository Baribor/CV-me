#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserService:
    @staticmethod
    def view_profile(user):
        profile_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
            'sex': user.sex,
            # Add more profile attributes as needed
        }
        return profile_data

    @staticmethod
    def edit_profile(user, new_data):
        for key, value in new_data.items():
            setattr(user, key, value)
        db.session.commit()

    @staticmethod
    def create_cv(user, cv_data):
        from models import CV  # Import your CV model
        cv = CV(title=cv_data.get('title', ''))
        user.cvs.append(cv)
        db.session.add(cv)
        db.session.commit()
        return cv

    @staticmethod
    def delete_cv(user, cv_id):
        cv = CV.query.get(cv_id)
        if cv and cv in user.cvs:
            user.cvs.remove(cv)
            db.session.delete(cv)
            db.session.commit()
            return True 
        return False  




