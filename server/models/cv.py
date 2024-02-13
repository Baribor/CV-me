#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base import BaseModel

class CV(BaseModel,Base):
    __tablename__ = 'cvs'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    createdAt = Column(DateTime, nullable=False)
    UpdateddAt = Column(DateTime, nullable=False)

    # Define the one-to-one relationships
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project', back_populates='cv')

    skill_id = Column(Integer, ForeignKey('skills.id'))
    skill = relationship('Skill', back_populates='cv')

    education_id = Column(Integer, ForeignKey('educations.id'))
    education = relationship('Education', back_populates='cv')

    experience_id = Column(Integer, ForeignKey('experiences.id'))
    experience = relationship('Experience', back_populates='cv')

    smart_url_id = Column(Integer, ForeignKey('smart_urls.id'))
    smart_url = relationship('SmartUrl', back_populates='cv')
