#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an email parameter and displays the response body.

Usage: ./6-post_email.py <URL> <email>

Arguments:
    URL (str): The URL to which the POST request will be sent.
    email (str): The email address to be sent as a parameter.

Example:
    ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email as a parameter
    data = {'email': email}

    # Send a POST request to the URL with the email parameter
    response = requests.post(url, data=data)

    # Display the email and response body
    print("Your email is:", email)
    print(response.text)
