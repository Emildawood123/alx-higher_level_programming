#!/usr/bin/python3
"""add email and show it"""
if __name__ == "__main__":
    from urllib import parse, request
    import sys
    quary_str = {'email': sys.argv[2]}
    data = parse.urlencode(quary_str)
    with request.urlopen(sys.argv[1], data=data) as url:
        r = url.read().decode('UTF-8')
        print(r)
