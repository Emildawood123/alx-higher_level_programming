#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""
if __name__ == "__main__":
    from urllib import request, error
    import sys
    with request.urlopen(sys.argv[1]) as url:
        try:
            print(url.read().decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
