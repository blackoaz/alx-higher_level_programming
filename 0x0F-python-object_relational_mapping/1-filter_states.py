#!/usr/bin/python3
"""Function for listing states that begin with capital N"""

from sys import argv
import MySQLdb


def get_states(username, password, database):
    """retrieving states with names begin with N"""

    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         password=str(password), database=str(database))
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id")

    [print(state) for state cur.fetchall() if state[1][0] = "N"]

    cur.close()
    db.close()


if __name__ == '__main__':
    get_states(argv[1], argv[2], argv[3])
