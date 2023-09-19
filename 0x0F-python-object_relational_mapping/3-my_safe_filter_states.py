#!/usr/bin/python3

"""
module securely checks value of a state
"""

import sys
import MySQLdb


def state_value(username, password, database, state_name):
    """
    Retrieve and display state information based on the given state_name.

    Args:
        username (str): MySQL username for database connection.
        password (str): MySQL password for database connection.
        database (str): Name of the MySQL database.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    # Create a connection to the MySQL database
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cursor = connection.cursor()
    # Use placeholders in the query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    # Fetch all rows from the result set
    states = cursor.fetchall()
    # Close cursor and connection
    cursor.close()
    connection.close()
    # Display the results
    for state in states:
        print(state)


if __name__ == "__main__":
    """
    Check if the correct number of command-line arguments is provided and
    execute the state_value function with the provided arguments.
    """
    if len(sys.argv) != 5:
        print("error")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # Call the function with the provided arguments
    state_value(username, password, database, state_name)
