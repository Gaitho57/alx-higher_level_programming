#!/bin/bash
# Bash script that takes URL and dispaying all HTTP method server acceps
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
