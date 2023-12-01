#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys
"""import urllib"""
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1], data="email={}".format(sys.argv[2])) as url:
       print(url.headers)
