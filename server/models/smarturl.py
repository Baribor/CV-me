#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from .base import Base
from models.user import User


db = SQLAlchemy()

class SmartUrl(db.Model):
    """Defines class model SmartUrl"""

    id = db.Column(db.Integer, primary_key=True)
    urlName = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(150), nullable=False)
    viewedAt = db.Column(db.Timestamp, nullable=False)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    cv = db.relationship('User.CV', back_populates='project')
