#!/usr/bin/python3
"""
Sends a POST request to a given URL 
with an email as a parameter and displays the response body.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    """
    where function executes
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        body = response.read()

    print(body.decode('utf-8'))
