#!/bin/bash
# sends a request to a URL passed as an argument, displays only d status code of d response
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
