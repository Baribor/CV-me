#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.base import BaseModel

class User(BaseModel,Base):
    __tablename__ = 'users'
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        cvs (list): List of CVs associated with the user.
    """
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(250), unique=True, nullable=False)
    first_name = Column(String(250), unique=True, nullable=False)
    last_name = Column(String(250), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String(50), nullable=False)

    cvs = relationship('CV', backref='user')
