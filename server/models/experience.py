#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models.base import BaseModel, Base

class Experience(BaseModel, Base):
    __tablename__ = 'experience'

    id = Column(Integer, primary_key=True)
    company = Column(String(150), nullable=False)
    position = Column(String(150), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(Integer, ForeignKey('cvs.cv_id'), nullable=False)
