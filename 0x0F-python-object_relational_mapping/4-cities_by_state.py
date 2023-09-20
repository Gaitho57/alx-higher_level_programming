#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def list_cities(username, password, database):
    """
    This function lists cities from the database
    """
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    query = 'SELECT * FROM cities ORDER BY id ASC'

    cursor.execute(query)

    cities = cursor.fetchall()

    cursor.close()
    connection.close()

    for city in cities:
        print(city)


if __name__ == '__main__':
    """
    main function where the code is executed
    """
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
