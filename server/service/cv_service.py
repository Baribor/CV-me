from models.base import Session
from models.cv import CV
from models.user import User

class CVService:
    @staticmethod
    def get_cv(user_id):
      user = Session().query(User).get(user_id)
      if not user:
        return None
      return Session().query(CV).filter_by(user_id=user_id).with_entities(CV.id, CV.title, CV.user_id, CV.createdAt, CV.UpdateddAt).all()


    @staticmethod
    def delete_cv(id):
        session = Session()
        cv = session.query(CV).get(id)
        if cv:
            session.delete(cv)
            session.commit()
            return True
        return False
    
    @staticmethod
    def edit_cv(id, new_data):
        session = Session()
        cv = session.query(CV).get(id)
        if not cv:
            return None
        for key, value in new_data.items():
            setattr(cv, key, value)
        session.commit()
        return cv
