#!/bin/bash
# cURL body content

curl -s -o "$1" /dev/null -w "%{http_code}" "$URL" | grep -q "200" && curl -s "$URL"
