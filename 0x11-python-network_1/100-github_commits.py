#!/usr/bin/python3
"""Write a Python script that takes in a URL..."""

if __name__ == "__main__":
    import requests
    import sys
    headers = {'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github.v3+json'}
    payload = {'per_page': 10, 'page': 1}
    res = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2],
                                                            sys.argv[1]),
        headers=headers,
        params=payload)
    for i in res.json():
        print("{}: {}".format(i['sha'], i['commit']['author']['name']))
