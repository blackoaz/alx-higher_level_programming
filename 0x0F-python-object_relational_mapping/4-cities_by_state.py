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


if __name__ = '__main__':
    get_cities(sys.argv[1], sys.argv[2], sys.argv[3])
