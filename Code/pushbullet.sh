#!/bin/bash
DAPI="ENTER YOUR API KEY"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type noted title="Alert" -d body=" $MSG"
