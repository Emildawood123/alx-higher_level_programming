#!/bin/bash
# this for get the size of content body
curl -sI "$1" | grep -i "allow" | cut -d ' ' -f -2
