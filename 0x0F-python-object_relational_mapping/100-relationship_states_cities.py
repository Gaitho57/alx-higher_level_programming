#!/usr/bin/python3
"""
Script that creates a State object with a City object in the database
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

    # Create a State object
    california = State(name="California")

    # Create a City object
    san_francisco = City(name="San Francisco")

    # Add the City object to the State object's cities relationship
    california.cities.append(san_francisco)

    # Add the State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to the database
    session.commit()

    # Close the session
    session.close()
