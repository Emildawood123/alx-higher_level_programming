#!/bin/bash
# this for get the size of content body
curl -sL -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
