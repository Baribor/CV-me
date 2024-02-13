#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base
from models.cv import CV

class Project(BaseModel,Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    projectName = Column(String(150), nullable=False)
    description = Column(String(150), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(Integer, ForeignKey('cvs.id'), nullable=False)
    cv = relationship('CV', back_populates='project')
