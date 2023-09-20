#!/usr/bin/python3
"""
Script that lists all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Retrieve all City objects and their corresponding State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the City objects with their corresponding State names
    for city in cities:
        state_name = city.state.name
        print(f"{city.id}: {city.name} -> {state_name}")

    # Close the session
    session.close()
