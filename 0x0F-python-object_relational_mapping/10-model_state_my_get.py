#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as an argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with the provided name
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        # Print the id of the retrieved State object
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
