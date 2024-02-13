#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base
from models.cv import CV

class Skill(BaseModel,Base):
    __tablename__ = 'skills'
    """Defines columns for skill class model"""
    id = Column(Integer, primary_key=True)
    skillName = Column(String(150), nullable=False)
    proficiency = Column(Integer, nullable=False)
    cv_id = Column(Integer, ForeignKey('cvs.id'), nullable=False)
    cv = relationship('CV', back_populates='skill')
