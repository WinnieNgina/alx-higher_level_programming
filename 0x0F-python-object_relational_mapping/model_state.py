#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Integer, String, Column

Base = declarative_base()
class State(Base):
    #The first attribute should be a table name
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)