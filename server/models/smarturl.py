#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base
from sqlalchemy.dialects.postgresql import UUID

class SmartUrl(BaseModel):
    __tablename__ = 'smart_urls'
    """Defines class model SmartUrl"""
    id = Column(UUID(as_uuid=True), primary_key=True)
    urlName = Column(String(150), nullable=False)
    url = Column(String(150), nullable=False)
    viewedAt = Column(TIMESTAMP, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.cv_id'), nullable=False)
