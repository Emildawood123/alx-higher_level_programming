#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""
import json


if __name__ == "__main__":
    import requests
    import sys
    dic = {"q": ""}
    if (sys.argv == 2):
        dic = {"q": sys.argv[1]}
    resp = requests.post("http://0.0.0.0:5000/search_user", json=dic)
    try:
        string = resp.json()
        if (string):
            print("[{}}] {}".format(string.get("id"), string.get("name")))
        else:
            print("No result")
    except json.JSONDecodeError:
        print("Not a valid JSON")
