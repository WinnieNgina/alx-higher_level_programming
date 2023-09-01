#!/usr/bin/python3

import urllib.request
'''
Module to fetch specified link
'''
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()
        decode_content = content.decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t-content: {content}")
        print(f"\t- utf8 content: {decode_content}")
