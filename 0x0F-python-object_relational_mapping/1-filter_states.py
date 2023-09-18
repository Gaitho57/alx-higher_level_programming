#!/usr/bin/python3
import MySQLdb
import sys
"""module lists all states starting
with N from the database hbtn_0e_0_usa"""


def N_states(username, password, database):
    """lists all states starting with N
username = mysql password
password = mysql password
database = database name"""
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)

    c = connection.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' "
              "ORDER BY id ASC")
    states = c.fetchall()

    for state in states:
        print(state)


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    N_states(username, password, database)
