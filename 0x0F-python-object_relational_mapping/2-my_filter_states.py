#!/usr/bin/python3

"""
Module that retrieves value of an argument
from a MySQL database.
"""

import sys
import MySQLdb


def retrieve_state_value(username, password, database, state_name):
    """
    Retrieves information of a state from the table.
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
    cursor.execute(query, (state_name,))
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
    state_name = sys.argv[4]

    retrieve_state_value(username, password, database, state_name)
