#!/usr/bin/python3
"""Function for listing all the cities in the database"""


import sys
import MySQLdb


def get_cities(username, password, database):
    """Function for retrieving all teh cities"""

    db = MySQLdb.connect(host="localhost", user=str(username), port=3306,
                         password=str(password), database=str(database))
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` ORDER BY `id` ASC")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()


if __name__ == '__main__':
    # Check if all 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        # Retrieve the command-line arguments
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Call the function to list cities
        get_cities(username, password, database)
