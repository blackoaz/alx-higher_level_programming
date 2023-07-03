#!/bin/bash

# Checking if a URL is provided as an argument
if [ $# -eq 0 ]; then
  echo "Error: No URL provided."
  exit 1
fi

url="$1"

# Send a DELETE request to the URL and store the response
response=$(curl -s -X DELETE "$url")

# Display the body of the response
echo "$response"

