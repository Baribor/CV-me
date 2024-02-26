from models.base import Session
from models.education import Education
from datetime import datetime

class EducationService:
    @staticmethod
    def create_education(institution=None, degree=None, startDate=None, endDate=None, cv_id=None):
        education = Education(institution=institution, degree=degree, startDate=datetime.strptime(
            startDate, "%Y-%m-%dT%H:%M:%S.%fZ"), endDate=datetime.strptime(endDate, "%Y-%m-%dT%H:%M:%S.%fZ"), cv_id=cv_id)
        Session().add(education)
        Session().commit()
        return education

    @staticmethod
    def get_education(education_id):
        education = Session().query(Education).get(education_id)
        return education.to_dict() if education else None

    @staticmethod
    def edit_education(education_id, new_data):
        education = Session().query(Education).get(education_id)
        if education:
            for key, value in new_data.items():
                setattr(education, key, value)
            Session().commit()
            return education
        return None

    @staticmethod
    def delete_education(education_id):
        education = Session().query(Education).get(education_id)
        if education:
            Session().delete(education)
            Session().commit()
            return True
        return False

