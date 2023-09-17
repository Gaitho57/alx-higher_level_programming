#!/usr/bin/python3
"""Module that lists all states from mySQL database"""
import sys
import MySQLdb

def list_states (username, password, database):
    """lists all states from the database hbtn_0e_0_usa.
    Ags:
        username: mysql username
        password: mysql password
        database: mysql database
    """
    # Connect to the MySQL server
    connection  = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
    c = connection.cursor()

    c.execute("SELECT * FROM states ORDER BY id ASC")

    states = c.fetchall()

    for state in states:
        print(state)
    
    connection.close()

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
