#!/bin/bash
# script to get body size of response
curl -Is "$1" | grep -w 'Content-Length' | cut -f2 -d' '
