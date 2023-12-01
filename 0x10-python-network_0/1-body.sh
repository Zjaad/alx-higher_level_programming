#!/bin/bash
#displays the body of the response (if status code is 200).
curl -sX GET $1 -L
