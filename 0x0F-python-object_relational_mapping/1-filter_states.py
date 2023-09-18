import MySQLdb
import sys
"""module lists all states starting
with N from the database hbtn_0e_0_usa"""


def N_states(username, password, database):
    """lists all states starting with N
username = mysql password
password = mysql password
database = database name"""
    cconnection = MySQLdb.connect(
        host='localhost',
        port=3306,  # Corrected the port number
        user=username,
        passwd=password,  # Corrected the argument name
        db=database)

    c = connection.cursor()
     c.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]

    c.close()
    connection.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    N_states(username, password, database)
