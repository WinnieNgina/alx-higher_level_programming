#!/usr/bin/python3
''''
class definition of a City and an instance Base = declarative_base()
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base, State

Base = declarative_base()


class City(Base):
    '''
    The first attribute should be a table name
    many to one relationship
    '''
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
