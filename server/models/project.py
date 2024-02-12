#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.base import BaseModel
from base import db


class Project(db.BaseModel):
    """Defines Project class model"""

    id = db.Column(db.Integer, primary_key=True)
    projectName = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    cv_id = db.Column(db.Integer, db.ForeignKey('user.cv.id'), nullable=False)
    cv = db.relationship('User.CV', back_populates='project')
