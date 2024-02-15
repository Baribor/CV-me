#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base
from sqlalchemy.dialects.postgresql import UUID

class Skill(BaseModel,Base):
    __tablename__ = 'skills'
    """Defines columns for skill class model"""
    id = Column(Integer, primary_key=True)
    skillName = Column(String(150), nullable=False)
    proficiency = Column(Integer, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.cv_id'), nullable=False)
