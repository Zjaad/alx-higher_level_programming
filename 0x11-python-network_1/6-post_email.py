#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response."""
import requests
import sys
if __name__ == "__main__":
    link = sys.argv[1]
    email= sys.argv[2]
    data = {'email': email}
    r = requests.post(link, data=data)
    print("Your email is: {}".format(r.text))
