#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    pas = argv[2]
    db = argv[3]
    dbUrl = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pas, db)
    engine = create_engine(dbUrl)
    Session = sessionmaker(bind=engine)  # returns a function
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))
