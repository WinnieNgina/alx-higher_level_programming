#!/usr/bin/python3
'''
Search API
'''
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': q}
    response = requests.post(url, data=params)
    try:
        json_res = response.json()
        if json_res:
            print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
