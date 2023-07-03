#!/bin/bash
# script for displaying allowed methods in a http request
#!/bin/bash
curl -sI "$1" | grep 'Allow' | cut -d " " -f 2-
