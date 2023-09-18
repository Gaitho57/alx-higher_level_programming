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
            host='localhost'
            port=3606
            user=username
            pssd=password
            db=database)

    c = connection.cursor()
    query = c.execute("SELECT * FROM states WHERE name LIKE 'N%' "
                      "ORDER BY id ASC")

    for state in query:
        print(state)

    c.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    N_states(username, password, database)
