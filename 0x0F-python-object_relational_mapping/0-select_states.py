#!/usr/bin/python3
"""a script to list all states from a database"""


import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    hostName = 'localhost'
    
    db = MySQLdb.connect(host=hostName, port=3306, user=username, password=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close
    db.close
