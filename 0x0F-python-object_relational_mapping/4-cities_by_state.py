#!/usr/bin/python3

"""
This script lists all cities from the database hbtn_0e_4_usa.

Usage: python3 script_name.py username password database
Example: python3 script_name.py myuser mypassword mydatabase

Requirements:
- The script should connect to a MySQL server running on localhost at port
    3306.
- Results must be sorted in ascending order by cities.id.
- The module MySQLdb is used for database connection (import MySQLdb).
- The execute() method is used only once.
- Results are displayed one row at a time.

"""

import sys
import MySQLdb

def list_cities(username, password, database):
    """
    Connects to the MySQL database and lists all cities.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

    Returns:
        None. Prints the cities directly.

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
    if len(sys.argv) != 4:
        print("Error: Invalid arguments")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
