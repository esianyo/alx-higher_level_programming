#!/bin/bash
# cURLs only methods
curl -s -IX OPTIONS "$1" | grep Allow | cut -d " " -f2
