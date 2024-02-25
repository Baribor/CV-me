#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from .base import BaseModel, Base
import uuid

class Project(BaseModel,Base):
    __tablename__ = 'projects'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    projectName = Column(String(150), nullable=False)
    description = Column(String(150), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.id'), nullable=False) 

    def to_dict(self):
        return {
            'id': self.id,
            'projectName': self.projectName,
            'description': self.description,
            'startDate': self.startDate.isoformat(),
            'endDate': self.endDate.isoformat(),
        }
