#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base

class Education(BaseModel,Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key=True)
    institution = Column(String(100), nullable=False)
    degree = Column(String(150), nullable=True)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(Integer, ForeignKey('cvs.cv_id'), nullable=False)
