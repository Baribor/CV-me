#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models.base import BaseModel, Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Experience(BaseModel, Base):
    __tablename__ = 'experience'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    company = Column(String(150), nullable=False)
    position = Column(String(150), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.cv_id'), nullable=False)
