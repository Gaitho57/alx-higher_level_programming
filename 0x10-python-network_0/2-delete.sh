#!/bin/bash
# DELETE requests passed as 1st arg and displays body of the reponse
curl -sX DELETE "$1"
