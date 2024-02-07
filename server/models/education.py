#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from .base import Base

db = SQLAlchemy()

class Education(db.Model):
    """Defines columns for education class"""

    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(150), nullable=True)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    cv = db.relationship('CV', back_populates='education')
