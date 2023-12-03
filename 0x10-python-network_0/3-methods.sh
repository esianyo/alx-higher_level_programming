#!/bin/bash
# cURLs only methods
curl -s -I "$1" | grep Allow | cut -c 8-
