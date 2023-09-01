#!/bin/bash
# Use curl to send a GET request and include the header
curl -X GET -H "X-School-User-Id: 98" "$1"
