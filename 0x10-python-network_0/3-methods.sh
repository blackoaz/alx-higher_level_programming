#!/bin/bash
# script for displaying allowed options in a http request
curl -sI "$1" | grep 'Allow' | cut -d "" -f 2-
