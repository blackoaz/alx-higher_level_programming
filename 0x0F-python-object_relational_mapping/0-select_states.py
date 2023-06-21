#!/usr/bin/python3
"""Script for listing all states in a database in a ascending order"""


import MySQLdb
from sys import argv


def get_states(username, password, database):
    """function for getting all the states"""
    db = MySQLdb.cnnect(host="localhost", port="3306", password=str(password),
                        user=str(username), database=str(database),
                        charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = curs.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()


if __name__ = '__main__':
    get_states(argv[1], argv[2], argv[3])
