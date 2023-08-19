#!/usr/bin/python3
"""
Lists states with a given name from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def main():
    """
    Connects to a MySQL server and displays all values in the states table
    where the name matches the provided argument.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute query to select states with the provided name and order by id
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
