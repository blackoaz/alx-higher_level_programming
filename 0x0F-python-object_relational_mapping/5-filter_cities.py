#!/usr/bin/python3
"""Selecting cities based on state"""

import sys
import MySQLdb


def select_city_by_state(username, password, database, state_name):
    """Selecting cities based on states"""

    db = MySQLdb.connect(host="localhost", user=str(username), port=3306,
                         password=str(password), database=str(databse))
    cur = db.cursor()
    cur.execute("SELECT * FROM cities WHERE state = %s ORDER BY id ASC",
                (state_name))
    cities = cur.fetchall()
    for city in cities:
        print(city)
    db.close()
    cur.close()


if __name__ == '__main__':
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script.py < username > < password > < database >
              < state_name >")
    else:
        # Retrieve the command-line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Call the function to list cities by state
        select_city_by_state(username, password, database, state_name)
