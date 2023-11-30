#!/bin/bash
# this for get the size of content body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
