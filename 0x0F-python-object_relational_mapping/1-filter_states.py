#!/usr/bin/python3

"""
Module to retrieve states from a MySQL database.
"""

import MySQLdb
import sys


def retrieve_states(username, password, database):
    """
    Retrieve states with names starting with 'N' from database.
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
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    retrieve_states(username, password, database)
