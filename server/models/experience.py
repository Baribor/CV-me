#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .base import BaseModel, Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class Experience(BaseModel, Base):
    __tablename__ = 'experience'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    company = Column(String(150), nullable=False)
    position = Column(String(150), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.id'), nullable=False)

    def to_dict(self):
        """Converts the Experience object to a dictionary."""
        start_date = datetime.strptime(self.startDate, '%Y-%m-%d')
        end_date = datetime.strptime(self.endDate, '%Y-%m-%d')

        return {
            'id': str(self.id),
            'company': self.company,
            'position': self.position,
            'startDate': self.startDate.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'endDate': self.endDate.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'cv_id': str(self.cv_id)
        }
