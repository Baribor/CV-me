#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel, Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Skill(BaseModel,Base):
    __tablename__ = 'skills'
    """Defines columns for skill class model"""
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    skillName = Column(String(150), nullable=False)
    proficiency = Column(Integer, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.id'), nullable=False)
