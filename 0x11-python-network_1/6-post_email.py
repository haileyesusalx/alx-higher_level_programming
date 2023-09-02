#!/usr/bin/python3
'''This script takes a URL and an email address as arguments,
sends a POST request with the email as a parameter,
and displays the email address from the response.
'''
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {"email": email}

    response = requests.post(url, data=data)

    # Extract and print the email from the response content
    print("Your email is: {}".format(response.text))
