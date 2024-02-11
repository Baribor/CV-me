#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from .base import Base
from models.user import User


db = SQLAlchemy()

class Skill(db.Model):
    """Defines columns for skill class model"""

    id = db.Column(db.Integer, primary_key=True)
    skillName = db.Column(db.String(150), nullable=False)
    proficiency = db.Column(db.Integer, nullable=False)
    cv_id = db.Column(db.Integer, db.ForeignKey('cv.id'), nullable=False)
    cv = db.relationship('User.CV', back_populates='skill')
