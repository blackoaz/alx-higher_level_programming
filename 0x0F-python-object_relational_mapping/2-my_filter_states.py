#!/usr/bin/python3
"""
Lists all states with name starting with N
"""

import MySQLdb
from sys import argv


def get_states(username, password, dbname):
    """listing all states with a name starting with N"""
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(dbname), charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states
                WHERE name LIKE BINARY '{}'".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    get_states(argv[1], argv[2], argv[3])
