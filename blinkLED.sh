#!/bin/bash

echo none | sudo tee /sys/class/leds/ACT/trigger

while true; do
    # Turn on the LED
    echo 1 | sudo tee /sys/class/leds/ACT/brightness
    sleep 1  # Wait for 1 second

    # Turn off the LED
    echo 0 | sudo tee /sys/class/leds/ACT/brightness
    sleep 1  # Wait for 1 second
done
