#!/usr/bin/python3
"""import some libraries"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State"""
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
