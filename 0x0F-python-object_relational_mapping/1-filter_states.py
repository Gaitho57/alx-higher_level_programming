"""
This module provides functions to retrieve states from a MySQL database.

It includes a function 'retrieve_states'
that retrieve states with names starting with 'N'
from a MySQL database and print them to the console.

Usage:
    $ python my_module.py <username> <password> <database>
"""

import MySQLdb
import sys


def retrieve_states(username, password, database):
    """
    Retrieve states with names starting with 'N'
    from the specified MySQL database.

    Args:
        username (str): The username to connect to the database.
        password (str): The password for the database user.
        database (str): The name of the database to connect to.

    Returns:
        None

    Prints the retrieved states to the console.
    """
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)

    c = connection.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    c.execute(query)
    states = c.fetchall()

    for state in states:
        print(state)

    c.close()
    connection.close()


if __name__ == '__main__':
    """
    Main function to execute the script.

    Usage:
        $ python my_module.py <username> <password> <database>
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    retrieve_states(username, password, database)
