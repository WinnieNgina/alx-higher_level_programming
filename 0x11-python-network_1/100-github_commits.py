#!/usr/bin/python3
'''
uses the GitHub API to retrieve the first 10 commits
'''

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo_name = sys.argv[1]
    user_name = sys.argv[2] 
    response = requests.get('https://developer.github.com/v3/repos/user_name/repo_name/commits/')
    commits_data = response.json()
    for commit in commits_data[:10]:  # Get the first 10 commits
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{}: {}".format(sha, author_name))
