#!/usr/bin/python3
'''
sends a request to the URL
Displays the value of the X-Request-Id
'''
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    params = {"email": sys.argv[2]}
    r = requests.post(url, data=params)
    print("{}".format(r.text))
