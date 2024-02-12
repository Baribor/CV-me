#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from base import BaseModel
from models.user import User
from base import db



class Education(db.BaseModel):
    """Defines columns for education class"""

    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(150), nullable=True)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    cv = db.relationship('User.CV', back_populates='education')
