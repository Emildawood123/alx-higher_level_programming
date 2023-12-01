#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""

if __name__ == '__main__':
    import sys
    import requests
    import json

    headers = {'Accept': 'application/vnd.github+json',
               'Authorization':  f'Bearer {sys.argv[2]}',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get('https://api.github.com/user', headers=headers,)
    try:
        json_text = res.json()
        if (json_text):
            print('{}'.format(json_text["id"]))
    except json.JSONDecodeError:
        print('there is not')
