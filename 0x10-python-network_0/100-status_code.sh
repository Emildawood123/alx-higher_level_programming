#!/bin/bash
# this for get the size of content body
curl -s -o /dev/null -I -w "%{http_code}" "$1"
