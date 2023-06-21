#!/usr/bin/python3
"""Function for listing states that begin with capital N"""

from sys import argv
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id")

    [print(state) for state cur.fetchall() if state[1][0] == "N"]
