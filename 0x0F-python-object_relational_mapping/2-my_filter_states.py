#!/usr/bin/python3
"""a script to list in a filtered manner"""


import sys
from sys import argv
import MySQLdb


if __name__ == "__main__":
    un = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    hN = 'localhost'

    db = MySQLdb.connect(host=hN, port=3306, user=un, password=pwd, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE\
                   name LIKE BINARY '{:s}'\
                   ORDER BY id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close
    db.close
