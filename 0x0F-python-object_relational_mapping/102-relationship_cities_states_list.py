#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """
    Connects to a MySQL server, retrieves and prints the City data with linked
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print City data with linked State
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        city_name = city.name
        state_name = city.state.name
        print(f"{city.id}: {city_name} -> {state_name}")

    session.close()
