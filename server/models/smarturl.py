#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base

class SmartUrl(BaseModel):
    __tablename__ = 'smart_urls'
    """Defines class model SmartUrl"""
    id = Column(Integer, primary_key=True)
    urlName = Column(String(150), nullable=False)
    url = Column(String(150), nullable=False)
    viewedAt = Column(TIMESTAMP, nullable=False)
    cv_id = Column(Integer, ForeignKey('cvs.cv_id'), nullable=False)
