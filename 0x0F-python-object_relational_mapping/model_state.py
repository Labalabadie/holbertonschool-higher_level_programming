#!/usr/bin/python3
""" states module """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, auto-generated=True, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
