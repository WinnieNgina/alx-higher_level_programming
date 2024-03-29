#!/usr/bin/python3
'''
sends a request to the URL
Displays the value of the X-Request-Id
'''
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            encode_response = response.read().decode('utf-8')
            print("{}".format(encode_response))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
