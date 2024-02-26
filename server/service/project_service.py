from flask import jsonify, request
from models.base import Session
from models.project import Project
from datetime import datetime
from api.v1.middlewares.authMiddleware import AuthMiddleware

class ProjectService:
    @staticmethod
    def create_project(projectName=None, description=None, startDate=None, endDate=None, cv_id=None):
        project = Project(projectName=projectName, description=description, startDate=datetime.strptime(
            startDate, "%Y-%m-%dT%H:%M:%S.%fZ"), endDate=datetime.strptime(endDate, "%Y-%m-%dT%H:%M:%S.%fZ"), cv_id=cv_id)
        Session().add(project)
        Session().commit()
        return project

    @staticmethod
    def get_project(project_id):
        project = Session().query(Project).get(project_id)
        return project.to_dict() if project else None

    @staticmethod
    def edit_project(project_id, new_data):
        project = Session().query(Project).get(project_id)
        if project:
            for key, value in new_data.items():
                setattr(project, key, value)
            Session().commit()
            return project
        return None

    @staticmethod
    def delete_project(project_id):
        project = Session().query(Project).get(project_id)
        if project:
            Session().delete(project)
            Session().commit()
            return True
        return False

