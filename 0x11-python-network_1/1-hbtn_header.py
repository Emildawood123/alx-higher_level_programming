#!/usr/bin/python3
import urllib.request
import sys
"""import urllib"""
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
       print(url.headers["X-Request-id"])
