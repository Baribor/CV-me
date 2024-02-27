#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel, Base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

class Education(BaseModel,Base):
    __tablename__ = 'education'

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    institution = Column(String(100), nullable=False)
    degree = Column(String(150), nullable=True)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    cv_id = Column(UUID(as_uuid=True), ForeignKey('cvs.id'), nullable=False)


    def to_dict(self):
        """Converts the Education object to a dictionary."""
        start_date_str = self.startDate
        end_date_str = self.endDate

        # Convert start date and end date strings to datetime objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

        return {
            'id': str(self.id),
            'institution': self.institution,
            'degree': self.degree,
            'startDate': self.startDate.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'endDate': self.endDate.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }
