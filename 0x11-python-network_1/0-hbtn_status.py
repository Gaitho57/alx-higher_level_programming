#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io using urllib"""
import urllib.request


def fetch_status():
    """fetchs status of the URL & sisplays the response body"""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == '__main__':
    fetch_status()
