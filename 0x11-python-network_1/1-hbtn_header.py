#!/usr/bin/python3
# script for displaying header content


import urllib.request
import sys
if __name__ == '__main__':
    url = sys.argv[1]
    urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(dict(response.headers).get("X-Request-Id"))
