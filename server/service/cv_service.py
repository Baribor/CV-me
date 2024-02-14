from flask_sqlalchemy import SQLAlchemy
from models.user import User 
from models.cv import CV


db = SQLAlchemy()

class CvService:
    @staticmethod
    def get_cv(user_id):
        user = User.query.get(user_id)
        if not user:
            return None
        return user.cvs

    @staticmethod
    def create_cv(user_id, cv_data):
        user = User.query.get(user_id)
        if not user:
            return None
        cv = CV(title=cv_data.get('title', ''))
        user.cvs.append(cv)
        db.session.add(cv)
        db.session.commit()
        return cv

    @staticmethod
    def delete_cv(cv_id):
        cv = CV.query.get(cv_id)
        if cv:
            db.session.delete(cv)
            db.session.commit()
            return True
        return False


























