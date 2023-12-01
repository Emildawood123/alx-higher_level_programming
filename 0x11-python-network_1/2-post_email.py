#!/usr/bin/python3
"""add email and show it"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    quary_str = {'email': sys.argv[2]}
    quary_str = urllib.parse.urlencode(quary_str)
    with urllib.request.urlopen(sys.argv[1], data=quary_str) as url:
        print(url.read().decode('utf-8'))
