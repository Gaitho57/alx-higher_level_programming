#!/bin/bash
# Bash Script that sends request and gives status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
