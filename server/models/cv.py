#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import BaseModel, Base
from .project import Project
from .education import Education
from .experience import Experience
from .skill import Skill
from .smarturl import SmartUrl
import uuid

class CV(BaseModel, Base):
    __tablename__ = 'cvs'

    # Define columns
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    title = Column(String(100), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    createdAt = Column(DateTime, nullable=False, default=func.now())
    UpdateddAt = Column(DateTime, nullable=False,
                        default=func.now(), onupdate=func.now())

    # Define relationships
    projects = relationship('Project', backref='cv')
    educations = relationship('Education', backref='cv')
    experiences = relationship('Experience', backref='cv')
    skills = relationship('Skill', backref='cv')
    smart_urls = relationship('SmartUrl', backref='cv')

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'user_id': str(self.user_id),
            'createdAt': self.createdAt.isoformat(),
            'updatedAt': self.UpdateddAt.isoformat(),
        }
