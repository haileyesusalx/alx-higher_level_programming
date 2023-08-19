#!/usr/bin/python3
"""
This script lists all states with names starting with 'N' from the database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Connects to a MySQL server, retrieves and prints states with names
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute query to select states with names starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
