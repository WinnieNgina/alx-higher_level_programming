#!/bin/bash
# Use curl to send a GET request and include the header
curl -sH "X-School-User-Id: 98" "$1"
