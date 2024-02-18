#!/usr/bin/python3
from models.base import Base, engine
from models.user import User
from models.cv import CV
from models.education import Education
from models.project import Project
from models.experience import Experience
from models.skill import Skill
from models.smarturl import SmartUrl

# Create tables in the database
def create_tables():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()
