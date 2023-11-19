#!/usr/bin/python3
"""Selects all cities by state"""

import sys
from sys import argv
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
        port=3306,
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities")

    rows = cursor.fetchall()

    for row in rows:
        city_id = row[0]
        city_name = row[1]
        state_id = row[2]

        cursor.execute("SELECT cities.id, cities.name, states.name\
                FROM `cities`\
                JOIN `states` ON state_id=states.id\
                ORDER BY cities.id")
        state_name = cursor.fetchone()[0]

        print(f"City: {city_name}, State: {state_name}")

    cursor.close()
    db.close()
