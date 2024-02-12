#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from mdels.base import BaseModel

class CV(db.BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    UpdateddAt = db.Column(db.DateTime, nullable=False)

    # Define the one-to-one relationships
    project = db.relationship('Project', uselist=False, back_populates='cv')
    skill = db.relationship('Skill', uselist=False, back_populates='cv')
    education = db.relationship('Education', uselist=False, back_populates='cv')
    experience = db.relationship('Experience', uselist=False, back_populates='cv')
    smart_url = db.relationship('SmartUrl', uselist=False, back_populates='cv')
