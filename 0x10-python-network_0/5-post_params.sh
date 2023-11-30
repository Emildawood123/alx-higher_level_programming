#!/bin/bash
# this for get the size of content body
curl -s -H "email: test@gmail.com" -h "subject: I will always be here for PLD" -X POST "$1"
