from models.base import Session
from models.project import Project
from datetime import datetime


class ProjectService:
    @staticmethod
    def create_project(projectName=None, description=None, startDate=None, endDate=None, cv_id=None):
        project = Project(projectName=projectName, description=description, startDate=datetime.strptime(
            startDate, "%Y-%m-%dT%H:%M:%S.%fZ"), endDate=datetime.strptime(endDate, "%Y-%m-%dT%H:%M:%S.%fZ"), cv_id=cv_id)
        Session().add(project)
        Session().commit()
        return project
