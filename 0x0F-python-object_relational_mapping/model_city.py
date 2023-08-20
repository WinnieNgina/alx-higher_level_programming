#!/usr/bin/python3
''''
class definition of a City and an instance Base = declarative_base()
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from model_state import Base, State
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    '''
    The first attribute should be a table name
    One to may relationship
    '''
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
