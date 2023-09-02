#!/usr/bin/python3
<<<<<<< HEAD
""" POST request to the passed URL  with the email as a parameter,
and finally displays the body of the response
"""

import sys
import requests
=======
"""
This script sends a POST request to a given URL with an email parameter and displays the response body.

Usage: ./6-post_email.py <URL> <email>

Arguments:
    URL (str): The URL to which the POST request will be sent.
    email (str): The email address to be sent as a parameter.
"""
import requests
import sys
>>>>>>> 788f58994ef1f4b35146593b22326447545dded6

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
<<<<<<< HEAD
    data = {"email": email}

    response = requests.post(url, data=data)
    print("Your email is: {}".format(response))
=======

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
>>>>>>> 788f58994ef1f4b35146593b22326447545dded6
