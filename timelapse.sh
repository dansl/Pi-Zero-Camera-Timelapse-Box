#!/bin/bash
#3600000ms = 1 hour timelapse, 2000ms = photo every 2 seconds.
HOW_LONG=3600000
HOW_OFTEN=2000
SAVE_DIR="/home/pi/photos"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$SAVE_DIR/$TIMESTAMP"

rpicam-still -n --timeout $HOW_LONG --timelapse $HOW_OFTEN -o "$SAVE_DIR/$TIMESTAMP/image%04d.jpg"
