#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from models.base import BaseModel, Base
from models.project import Project
from models.education import Education
from models.experience import Experience
from models.skill import Skill
from models.smarturl import SmartUrl

class CV(BaseModel, Base):
    __tablename__ = 'cvs'

    # Define columns
    id = Column(UUID(as_uuid=True), primary_key=True,unique=True)
    title = Column(String(100), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    createdAt = Column(DateTime, nullable=False)
    UpdateddAt = Column(DateTime, nullable=False)

    # Define relationships
    projects = relationship('Project', backref='cv')
    educations = relationship('Education', backref='cv')
    experiences = relationship('Experience', backref='cv')
    skills = relationship('Skill', backref='cv')
    smart_urls = relationship('SmartUrl', backref='cv')

    def to_dict(self):
        return {
            'cv_id': str(self.cv_id),
            'title': self.title,
            'user_id': str(self.user_id),
            'createdAt': self.createdAt.isoformat(),
            'UpdateddAt': self.UpdateddAt.isoformat(),
        }
