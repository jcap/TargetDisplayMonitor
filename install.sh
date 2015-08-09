#!/bin/sh

cp targetdisplaymonitor.py /usr/local/bin/

cp com.user.targetdisplaymonitor.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.user.targetdisplaymonitor.plist
