#!/usr/bin/python3

"""
Module that retrieves value of an argument
from a MySQL database
"""

import sys
import MySQLdb


def retrieve_statevalue(username, password, database, statename):
    """
    retrieves information of a state from the table
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
