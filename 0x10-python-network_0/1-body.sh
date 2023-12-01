#!/bin/bash
#displays the body of the response (if status code is 200).
curl -s -X GET "$1" -o /dev/null -w '%{http_code}' | grep "200" && curl -s "$1"
