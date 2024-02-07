#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from models.user import User 
from models.project import Project
from models.education import Education
from models.base import Base


# Define your PostgreSQL connection string
DB_URI = 'postgresql://cv_me_local:cv_me_pwd@localhost:5432/cv_me_local'

# Create SQLAlchemy engine
engine = create_engine(DB_URI)
print("Engine:", engine)

# Create a metadata instance
metadata = MetaData(schema="cv_me_local")

# Bind the engine and metadata
metadata.bind = engine
print("Metadata:", metadata)

# Create tables based on your models
Base.metadata.create_all(engine)

print("Tables created successfully.")

