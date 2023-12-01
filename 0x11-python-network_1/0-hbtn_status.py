#!/usr/bin/python3
import urllib.request
"""import urllib"""
if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as url:
        text = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(text)))
        print("\t- content: {}".format(text))
        print("\t- utf8 content: {}".format(text.decode('utf-8')))
