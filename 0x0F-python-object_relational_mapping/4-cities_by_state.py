#!/usr/bin/python3
"""Selct cities by state"""


import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        host="localhost",
        port=3306
        )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)
    cursor.close()
    db.close()
