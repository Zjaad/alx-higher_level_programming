#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using the package requests."""
import requests
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(link)
    b = r.text
    print("Body response:")
    print("\t- type: {}".format(type(b)))
    print("\t- content: {}".format(b))
