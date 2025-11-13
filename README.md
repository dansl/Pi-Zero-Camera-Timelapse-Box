# Pi Camera Timelapse Box
***WORK IN PROGRESS***

Setup a Raspberry Pi Zero (or any Pi) with a camera module and a momentary push button, for a one click one hour timelapse taking a photo every 2 seconds!

## Hardware
- Raspberry Pi Zero or any Pi
- Raspberry Pi Camera Module
- Momentary push-button switch (Requires Soldering)
- UPS Battery Module (Optional)
- SD Card 32GB or more recommended.

## My Setup
- [Raspberry Pi Zero 2W](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)
- [Raspberry Pi Camera Module 3 (Autofocus)](https://www.raspberrypi.com/products/camera-module-3/)
- [Waveshare UPS HAT](https://www.waveshare.com/ups-hat-c.htm)
- [Momentary Push-Button Switch 6x6x12.5mm](https://www.digikey.com/en/product-highlight/s/schurter/6-mm-x-6-mm-tact-switches)
- [3D Printed Top](https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/3D%20Print/Top.stl)
- [3D Printed Bottom](https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/3D%20Print/Bottom.stl)

## Steps
- Solder the Momentary Push Button Switch across GPIO pins 37 and 39. (See Images Below, 37=GPIO26 and 39=Ground)
- [Setup Raspian OS](https://www.raspberrypi.com/documentation/computers/getting-started.html) on your SD Card. (If using a Pi Zero, use the "Lite" OS for better performance.)
- Access the devices command line, either via SSH or with a monitor, mouse and keyboard. Enter the commands below.
- Place the 3 Scripts from this repo into your Home folder. ("/home/pi/" unless you setup a different username)
	- ```wget https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/blinkLED.sh && wget https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/timelapse.sh && wget https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/button.py```
- Make them executable:
	- ```chmod +x timelapse.sh && chmod +x button.py && chmod +x blinkLED.sh```
- Setup a cron job to run the "button.py" script on boot. 
	- ```crontab -e``` 
	- If it asks about selecting an editor, just push Enter to use default "nano"
	- Paste this at the bottom of the file, make sure the path looks correct: ```@reboot python3 /home/pi/button.py```
	- Press Ctrl+X then Y then Enter to exit.
- Reboot
	- ```sudo reboot```
- Once booted, you should now be able to press the button to start taking a timelapse. The Green LED will slowly blink on and off on the Pi Zero indicating it's working and taking photos, if the light is steady or off completely, then it's probobly not working...
	- All photos will be placed into a "photos" folder in your Home folder (/home/pi/photos). 
	- The script will create a folder with the current time and date you clicked the button, and numberically add photos to that folder as it takes them. (See screenshot below)
	- If you click the button again, it should stop the timelapse, and the LED on the Pi will stop blinking on and off slowly.
	- Every time you start the Timelapse, it will create a new folder with the current date and time where it will dump all photos taken.

## Photos
![Screenshot](https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/photos/screenshot.png)
![Photo 0](https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/photos/photo0.jpeg)
![Photo 1](https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/photos/photo1.jpeg)
![Photo 2](https://github.com/dansl/Pi-Zero-Camera-Timelapse-Box/raw/refs/heads/main/photos/photo2.jpeg)
