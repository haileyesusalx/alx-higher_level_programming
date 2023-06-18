#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL server and lists all states from the specified database.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the query to select all states and order by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
