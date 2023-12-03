#!/bin/bash
# cURLs only methods
URL=$1
curl -s -I -X OPTIONS "$URL" | grep Allow | cut -d " " -f2
