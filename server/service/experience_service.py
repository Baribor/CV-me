from models.base import Session
from models.experience import Experience  # Import Experience model
from datetime import datetime

class ExperienceService:
    @staticmethod
    def create_experience(company=None, position=None, startDate=None, endDate=None, cv_id=None):
        experience = Experience(company=company, position=position, startDate=datetime.strptime(
            startDate, "%Y-%m-%dT%H:%M:%S.%fZ"), endDate=datetime.strptime(endDate, "%Y-%m-%dT%H:%M:%S.%fZ"), cv_id=cv_id)
        Session().add(experience)
        Session().commit()
        return experience

    @staticmethod
    def get_experience(experience_id):
        experience = Session().query(Experience).get(experience_id)  
        return experience.to_dict() if experience else None

    @staticmethod
    def edit_experience(experience_id, new_data):
        experience = Session().query(Experience).get(experience_id) 
        if experience:
            for key, value in new_data.items():
                setattr(experience, key, value)
            Session().commit()
            return experience
        return None

    @staticmethod
    def delete_experience(experience_id):
        session = Session()
        experience = session.query(Experience).get(experience_id)  
        if experience:
            session.delete(experience)
            session.commit()
            return True
        return False
    
    @staticmethod
    def find_first(**kwargs):
        session = Session()
        experience = session.query(Experience).filter_by(**kwargs).first()
        return experience
