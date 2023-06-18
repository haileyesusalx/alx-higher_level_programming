#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <database>")
        sys.exit(1)

    # Extract the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine and bind it to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Retrieve all State objects with a name containing the letter "a"
    states = session.query(State).filter(State.name.like("%a%")).all()

    # Delete the states
    for state in states:
        session.delete(state)

    # Commit the session to persist the changes
    session.commit()
