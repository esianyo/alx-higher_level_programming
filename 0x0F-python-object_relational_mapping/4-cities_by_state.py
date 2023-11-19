#!/usr/bin/python3
"""Selects all cities by state"""

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
        port=3306,
    )

    cursor = db.cursor()

    # Select all cities from the cities table
    cursor.execute("SELECT * FROM cities")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Iterate over the rows and print each city
    for row in rows:
        city_id = row[0]
        city_name = row[1]
        state_id = row[2]

        # Get the state name for the current city
        cursor.execute(
            f"SELECT name FROM states WHERE id = {state_id}"
        )
        state_name = cursor.fetchone()[0]

        print(f"City: {city_name}, State: {state_name}")

    cursor.close()
    db.close()
