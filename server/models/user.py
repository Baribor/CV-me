#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from models.base import BaseModel,Base

class User(BaseModel, Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(250), unique=True, nullable=False)
    first_name = Column(String(250), unique=True, nullable=False)
    last_name = Column(String(250), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String(50), nullable=False)

    cvs = relationship('CV', backref='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'sex': self.sex
        }
