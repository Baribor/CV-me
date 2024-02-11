#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy
from .base import Base
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class User(db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        cvs (list): List of CVs associated with the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(250),unique=True,nullable=False)
    first_name = db.Column(db.String(250),unique=True,nullable=False)
    last_name = db.Column(db.String(250),unique=True,nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(50), nullable=False)
    
class CV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    UpdateddAt = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref=db.backref('cvs', lazy=True))

