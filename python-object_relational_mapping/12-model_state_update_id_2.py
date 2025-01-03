#!/usr/bin/python3

"""
a script that changes the name of a
State object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter_by(id=2)
        .first()
        )

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
