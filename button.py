import os
import subprocess
import time

import psutil
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Disable LED
os.system("echo none | sudo tee /sys/class/leds/ACT/trigger")
os.system("echo 0 | sudo tee /sys/class/leds/ACT/brightness")


# print("Ready for button press...")
def button_pressed(channel):
    # print("Button pressed!")
    if is_process_running("rpicam-still"):
        # print("Stop Camera")
        os.system("pkill -f rpicam-still")
        os.system("pkill -f blinkLED.sh")
        os.system("echo 0 | sudo tee /sys/class/leds/ACT/brightness")
    else:
        # print("Run Camera")
        subprocess.Popen("/home/pi/timelapse.sh", shell=False)
        subprocess.Popen("/home/pi/blinkLED.sh", shell=False)


def is_process_running(name):
    for proc in psutil.process_iter(["name"]):
        if proc.info["name"] and name.lower() in proc.info["name"].lower():
            return True
    return False


GPIO.add_event_detect(37, GPIO.FALLING, callback=button_pressed, bouncetime=300)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
