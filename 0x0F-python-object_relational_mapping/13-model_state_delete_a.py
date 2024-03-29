#!/usr/bin/python3
"""
Deletes all state objects with a name containing a specific letter
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    for state in session.query(State).filter(State.name.like("%a%")).all():
        session.delete(state)
    session.commit()
    session.close()
