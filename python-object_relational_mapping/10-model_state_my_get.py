#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == "__main__":
    engine = create_engine(F"mysql+mysqldb://{argv[1]}:{argv[2]}\
                            @localhost/{argv[3]}")
    with Session(engine) as session:
        states = session.query(State).filter(State.name == argv[4].first())
        is states:
            print(F"{states.id}")
        else:
            print("Not found")
