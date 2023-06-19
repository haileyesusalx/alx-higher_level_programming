#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to a MySQL server and lists all cities of a given
    state from the hbtn_0e_4_usa database.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Prepare the query to select cities of the given state
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows and store the city names in a list
    cities = [row[0] for row in cursor.fetchall()]

    # Print the cities separated by commas
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
