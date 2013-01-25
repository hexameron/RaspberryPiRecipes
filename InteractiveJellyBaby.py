import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:
        if GPIO.input(4):
                os.system('mpg321 1748.mp3 &')
        sleep(1);
