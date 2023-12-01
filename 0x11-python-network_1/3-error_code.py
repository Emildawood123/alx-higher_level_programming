#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as url:
        try:
            print(url.read().decode('utf-8'))
        except urllib.error.HTTPError:
            print("Error code: {}".format(url.status))
