#!/usr/bin/python3
"""
Script that changes the name of a State object in the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Retrieve the State object with id = 2
    state = session.query(State).get(2)

    # Change the name of the State
    state.name = "New Mexico"

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
