#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""


if __name__ == "__main__":
    import requests
    import sys
    if (len(sys.argv) == 2):
        dic = {'q': sys.argv[1]}
    else:
        dic = {'q': ''}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=dic)
    try:
        string = resp.json()
        if (string):
            print("[{}}] {}".format(string["id"], string["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
