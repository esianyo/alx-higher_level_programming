#!/bin/bash
# cURLs only methods
curl -s -I -X OPTIONS "$1" | grep Allow | cut -d " " -f2
