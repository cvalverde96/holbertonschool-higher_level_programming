#!/usr/bin/python3

"""
a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa:
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    results = (
        session.query(State, City)
        .join(City)
        .order_by(City.id)
        .all()
        )

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
