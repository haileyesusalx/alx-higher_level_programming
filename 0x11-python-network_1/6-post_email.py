#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary to hold the email as a parameter
    data = {'email': email}

    # Send a POST request to the URL with the email as a parameter
    response = requests.post(url, data=data)

    print("Your email is:", email)
    print(response.text)

