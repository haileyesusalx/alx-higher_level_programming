#!/usr/bin/python3
"""
Script that fetches and prints all City objects
from the database hbtn_0e_14_usa
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: ./14-model_city_fetch_by_state.py <username> <password>'
              '<database>')
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
       username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id,
                           City.name).join(City).order_by(City.id).all()

    for city in cities:
        print(f'{city[0]}: ({city[1]}) {city[2]}')
