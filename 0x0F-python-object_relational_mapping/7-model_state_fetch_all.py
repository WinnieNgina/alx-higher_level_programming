#!/usr/bin/python3


'''
Retrieves lists all State objects from the database hbtn_0e_6_us
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    user = argv[1]
    pas = argv[2]
    db = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, pas, db), pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    """
    session maker returns a function
    """
    session = Session()

    for insitance in session.query(State).order_by(State.id):
        print("{}: {}".format(inistance.id, inistance.name))

    session.close()
