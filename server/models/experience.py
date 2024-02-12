#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from base import Base
from models.user import User
from base import db


class Experience(db.Model):
    """Defines columns for model class"""

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(150), nullable=False)
    position = db.Column(db.String(150), nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    cv = db.relationship('User.CV', back_populates='experience')
