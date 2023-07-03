#!/bin/bash
# script for calling  a url and checking the size in bytes
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
