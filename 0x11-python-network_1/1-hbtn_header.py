#!/usr/bin/python3
"""Write a Python script that takes in a URL,
 sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response."""
if __name__ == "__main__":
    import urllib.request
    import sys
    """import urllib"""
    with urllib.request.urlopen(sys.argv[1]) as url:
        print(url.headers["X-Request-id"])
