#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using the package requests."""
import requests
import sys
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(link)
    b = r.text
    print("Body response:")
    print(f"\t- type: {type(b)}")
    print(f"\t- content: {b}")
