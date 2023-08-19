#!/usr/bin/python3
"""
This module defines the City class and its attributes for the database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    City class for representing cities in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


# This code is not executed when imported
if __name__ == "__main__":
    pass
