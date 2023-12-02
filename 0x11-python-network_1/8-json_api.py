#!/usr/bin/python3
"""takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a param."""
import requests
import sys
if __name__ == "__main__":
    link = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}
    try:
        r = requests.post(link, data=data)
        jr = r.json()
        if not jr :
            print("No result")
        else :
            print("[{}] {}".format(jr.get('id'), jr.get('name')))
    except ValueError:
        print("Not a valid JSON")
