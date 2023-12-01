#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""
if __name__ == "__main__":
    import requests
    import sys
    dic = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], dic=dic)
    print(res.text)
