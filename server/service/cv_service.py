from models.base import Session
from models.cv import CV
from models.user import User

class CVService:
    @staticmethod
    def get_cv(user_id):
        user = Session().query(User).get(user_id)
        if not user:
            return None
        return user.cvs

    @staticmethod
    def create_cv(user_id, cv_data):
        user = Session().query(User).get(user_id)
        if not user:
            return None
        cv = CV(title=cv_data.get('title', ''))
        user.cvs.append(cv)
        Session().add(cv)
        Session().commit()
        return cv

    @staticmethod
    def delete_cv(cv_id):
        cv = Session().query(CV).get(cv_id)
        if cv:
            Session().delete(cv)
            Session().commit()
            return True
        return False
    
    @staticmethod
    def edit_cv(cv_id, new_data):
        cv = Session().query(CV).get(cv_id)
        if not cv:
            return None
        for key, value in new_data.items():
            setattr(cv, key, value)
        Session().commit()
        return cv
