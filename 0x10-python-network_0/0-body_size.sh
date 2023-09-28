#!/bin/bash
#Recieves URL and send a request to it
curl -s "$1" | wc -c
