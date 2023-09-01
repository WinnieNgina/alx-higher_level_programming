#!/usr/bin/python3
'''
sends a request to the URL
Displays the value of the X-Request-Id
'''
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.getheader('X-Request-Id')
        if header:
            print("{}".format(header))