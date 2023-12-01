#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""
if __name__ == "__main__":
    from urllib import request, error
    import sys
    with request.urlopen(sys.argv[1]) as url:
        try:
            r = url.read().decode('UTF-8')
            print(r)
        except error.HTTPError as err:
            print("Error code: {}".format(err.status))
