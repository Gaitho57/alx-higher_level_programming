#!/usr/bin/python3
import MySQLdb
import sys

def main():
    """
    Access data from the database and print states.
    
    Usage: python script.py <mysql_username> <mysql_password> <database_name>
    """
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        connection = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            password=mysql_password,
            db=database_name,
            port=3306
        )
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM states ORDER BY id ASC')

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
