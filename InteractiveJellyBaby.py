import time
import os
import RPi.GPIO

RPi.GPIO.setmode(GPIO.BCM)
RPi.GPIO.setup(4, GPIO.IN)
RPi.GPIO.setup(24, GPIO.IN)
RPi.GPIO.setup(25, GPIO.IN)

while True:
        if RPi.GPIO.input(4):
                os.system('mpg321 ow.mp3 &')
        sleep(1);
