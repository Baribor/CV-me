#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(Base):
    """
    Represents a base model in the system.

    Attributes:
        id (int): The unique identifier for the model.
    """
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
