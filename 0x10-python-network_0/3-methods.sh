#!/bin/bash
# cURLs only methods
curl -s -I -X "$1" | grep Allow | cut -c 8-
