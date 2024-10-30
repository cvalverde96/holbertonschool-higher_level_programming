#!/usr/bin/python3

"""
a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == state_name)
        .first()
        )

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
