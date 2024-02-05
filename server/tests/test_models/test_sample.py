# tests/test_simple.py
from flask_sqlalchemy import SQLAlchemy

def test_import():
    assert SQLAlchemy is not None
