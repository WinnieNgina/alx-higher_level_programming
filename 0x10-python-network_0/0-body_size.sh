#!/bin/bash
# Displays the number of bytes for a response

curl -s "$1" |wc -c
