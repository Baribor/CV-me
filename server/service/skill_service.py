from models.base import Session
from models.skill import Skill
from datetime import datetime

class SkillService:
    @staticmethod
    def create_skill(skillName=None, proficiency=None, cv_id=None):
        skill = Skill(skillName=skillName, proficiency=proficiency, cv_id=cv_id)
        session = Session()
        session.add(skill)
        session.commit()
        return skill

    @staticmethod
    def get_skill(skill_id):
        skill = Session().query(Skill).get(skill_id)
        return skill.to_dict() if skill else None

    @staticmethod
    def edit_skill(skill_id, new_data):
        skill = Session().query(Skill).get(skill_id)
        if skill:
            for key, value in new_data.items():
                setattr(skill, key, value)
            Session().commit()
            return skill
        return None

    @staticmethod
    def delete_skill(skill_id):
        skill = Session().query(Skill).get(skill_id)
        if skill:
            Session().delete(skill)
            Session().commit()
            return True
        return False

    @staticmethod
    def find_first(**kwargs):
        session = Session()
        skill = session.query(Skill).filter_by(**kwargs).first()
        return skill

