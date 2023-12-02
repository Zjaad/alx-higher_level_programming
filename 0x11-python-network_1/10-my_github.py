#!/usr/bin/python3
"""Displays github user's API"""
import requests
from requests.auth import HTTPBasicAuth
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    link = 'https://api.github.com/user'
    try:
        id = requests.get(link, auth=HTTPBasicAuth(username, password)).json().get('id')
        print(id if id else None)

    except ValueError:
        print(None)
