#!/bin/bash
# Bash script that takes URL, sends POST request, and outputs  response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
