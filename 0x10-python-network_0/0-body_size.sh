#!/bin/bash
# this for get the size of content body
curl -sI "$1" | grep -i content-length: | cut -d ' ' -f 2
