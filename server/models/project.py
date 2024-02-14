#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from models.base import BaseModel,Base

class Project(BaseModel,Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    projectName = Column(String(150), nullable=False)
    description = Column(String(150), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.cv_id'), nullable=False) 
