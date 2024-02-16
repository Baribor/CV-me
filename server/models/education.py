#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Education(BaseModel,Base):
    __tablename__ = 'education'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    institution = Column(String(100), nullable=False)
    degree = Column(String(150), nullable=True)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.cv_id'), nullable=False)
