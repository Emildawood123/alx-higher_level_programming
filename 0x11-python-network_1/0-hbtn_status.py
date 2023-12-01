#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    """import urllib"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as url:
        text = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(text)))
        print("\t- content: {}".format(text))
        print("\t- utf8 content: {}".format(text.decode('utf-8')))
