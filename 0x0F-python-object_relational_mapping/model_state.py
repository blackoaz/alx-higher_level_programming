#!/usr/bin/python3
"""
Script creating the model class for state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for MySQL database

    Attributes:
        id (str): The states's id
        name : The state's name.
        state_id: The city's state id.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
