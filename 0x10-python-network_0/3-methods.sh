#!/bin/bash
# this for get the size of content body
curl -sI "$1" | grep -i "allow" | awk -F ": " '{print $2}'
