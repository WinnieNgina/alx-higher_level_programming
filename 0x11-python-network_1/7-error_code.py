#!/usr/bin/python3
'''
sends a request to the URL
Displays the value of the X-Request-Id
'''
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
