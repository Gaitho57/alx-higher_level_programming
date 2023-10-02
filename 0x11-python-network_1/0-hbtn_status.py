#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io/status using urllib.
Prints the body response including the type,
content in bytes, and UTF-8 content.
"""
import urllib.request


def fetch_status():
    """
    Fetches the status of the URL and prints the body response.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))


if __name__ == "__main__":
    """
    where program begins to execute
    """
    fetch_status()
