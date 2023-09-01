#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an email parameter and displays the response body.

Usage: ./6-post_email.py <URL> <email>

Arguments:
    URL (str): The URL to which the POST request will be sent.
    email (str): The email address to be sent as a parameter.
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

    try:
        # Send a POST request to the URL with the email parameter
        response = requests.post(url, data=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Your email is:", email)
            print(response.text)
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
