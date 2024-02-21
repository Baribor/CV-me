#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from .base import BaseModel, Base
import datetime
import jwt

class User(BaseModel, Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)
    sex = Column(String(50), nullable=True)

    cvs = relationship('CV', backref='user')

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'sex': self.sex
        }

    def set_password(self, password):
        from api.v1.app import bcrypt
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        from api.v1.app import bcrypt
        print(self.password_hash)
        return bcrypt.check_password_hash(self.password_hash, password)

    def encode_auth_token(self):
        """
        Generates the Auth Token
        :return: string
        """
        from api.v1.app import app
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3),
                'iat': datetime.datetime.utcnow(),
                'sub': self.username
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
