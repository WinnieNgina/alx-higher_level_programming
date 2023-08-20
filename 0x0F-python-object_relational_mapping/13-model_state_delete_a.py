#!/usr/bin/python3

"""
Module that connects python script to a database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    check = 'a'
    query = (
            session.query(State)
            .filter(State.name.like('%{}%'.format(check)))
            .order_by(State.id)
            )
    for instance in query:
        session.delete(instance)
    session.commit()
    session.close()