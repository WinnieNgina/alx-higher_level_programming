#!/usr/bin/python3
'''
sends a request to the URL
Displays the value of the X-Request-Id
'''
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print("{}".format(r.headers.get("X-Request-Id")))
