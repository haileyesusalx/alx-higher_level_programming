#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header of the response.
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
