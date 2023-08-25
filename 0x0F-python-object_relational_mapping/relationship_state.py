#!/usr/bin/python3
''''
class definition of a State and an instance Base = declarative_base()
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from relationship_city import Base, City

# Base = declarative_base()


class State(Base):
    '''
    The first attribute should be a table name
    '''
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
