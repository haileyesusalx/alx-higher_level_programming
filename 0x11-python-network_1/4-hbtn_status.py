#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    # Send a GET request to the URL
    response = requests.get(url)

    # Display the response body in the specified format
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
