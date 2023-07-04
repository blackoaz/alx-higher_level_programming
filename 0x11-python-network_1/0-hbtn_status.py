#!/usr/bin/python3
# script for fetching a url content
import urllib.request


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body}\n\t- utf8 content: {body}")
