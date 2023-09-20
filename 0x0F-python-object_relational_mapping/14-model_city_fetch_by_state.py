#!/usr/bin/python3
"""
Script that prints all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Query City objects and order by id
    cities = session.query(City).order_by(City.id).all()

    # Print City objects grouped by the corresponding State name
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    # Close the session
    session.close()
