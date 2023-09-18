#!/usr/bin/python3

"""
This module retrieves the value of an argument from a MySQL database.

Usage:
    python3 3-select_states.py [username] [password] [database] [state name]

Arguments:
    username -- The MySQL username.
    password -- The MySQL password.
    database -- The name of the database.
    state name -- The name of the state to search for.

Requirements:
    - The module uses the MySQLdb library (import MySQLdb).
    - It connects to a MySQL server running on localhost at port 3306.
    - The SQL query is created using the provided user input with.
    - The results are sorted in ascending order by states.id.
    - The retrieved values are displayed as they are in the example output.
    - The script is not executed when imported.

Example:
    $ python3 3-select_states.py root password mydatabase "New York"
    (1, 'New York')
"""

import sys
import MySQLdb


def retrieve_statevalue(username, password, database, statename):
    """
    Retrieves information of a state from the table.

    Arguments:
        username -- The MySQL username.
        password -- The MySQL password.
        database -- The name of the database.
        state_name -- The name of the state to search for.
    """
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (statename,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    """
    Main function to execute the script.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    retrieve_statevalue(username, password, database, statename)
