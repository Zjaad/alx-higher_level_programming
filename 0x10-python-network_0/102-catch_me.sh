#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me, causing the server to respond with a message.
curl -o /dev/null -sw "You got me!" "0.0.0.0:5000/catch_me"
