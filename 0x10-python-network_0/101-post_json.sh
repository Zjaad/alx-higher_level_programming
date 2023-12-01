#!/bin/bash
#Script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

url="$1"
jsonFile="$2"
curl -sX POST "$url" -H "Content-Type: application/json" -d @"$jsonFile" -L
