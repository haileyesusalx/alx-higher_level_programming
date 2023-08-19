#!/usr/bin/python3
"""
Lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def filter_states_by_name_starting_with_n(username, password, database):
    """
    Retrieves and prints all states with names starting with 'N' from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute query to select states with name starting with N and order by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    """
    Main function to execute the script when run as the main program.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to filter and print states
    filter_states_by_name_starting_with_n(username, password, database)
