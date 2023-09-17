#!/usr/bin/python3
import MySQLdb
import sys

'''this modue takes arguments from the command line
it access data from the database and gives output of states'''

mysql username = sys.argv[1]
mysql password = sys.argv[2]
database name = sys.argv[3]

connection = MySQLdb.connect(
        host = localhost
        user = mysql username
        password = mysql password
        db = database name
        port = 3306
        )
c = connection.cursor()

c.execute('SELECT * FROM states ORDER BY states.id ASC')

states = c.fetchall

for state in states:
    print(state)

cursor.close()
connection.close()
