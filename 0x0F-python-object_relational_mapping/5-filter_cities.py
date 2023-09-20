#!/usr/bin/python3

"""
Module that lists all cities in the specified state from the database.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    # and connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities in the specified state
    query = ("SELECT * FROM `cities` as `c` "
             "INNER JOIN `states` as `s` "
             "ON `c`.`state_id` = `s`.`id` "
             "ORDER BY `c`.`id`")
    cursor.execute(query)

    # Fetch all rows and filter cities by the specified state
    # and print the cities separated by commas
    cities = [city[2] for city in cursor.fetchall() if city[4] == sys.argv[4]]
print(", ".join(cities))
