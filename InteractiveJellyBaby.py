# Import the Python libraries that we need for this program
import time
import os
import RPi.GPIO as GPIO

# Set-up the General Purpose Input-Ouput (GPIO) pins
GPIO.cleanup() # Start from scratch
GPIO.setmode(GPIO.BCM) # Set GPIO mode for the Pi
GPIO.setup(2, GPIO.IN) # Set Pin 2 on the GPIO header to be an input

# This loop runs forever and plays the mp3 file when the two wires are touching
while True: # Loop forever
        if GPIO.input(2) == False: # Check to see if GPIO pin 2 is connected to the ground pin
                os.system('mpg321 1748.mp3 &') # If it is then play the mp3 file
        time.sleep(1); # Wait for a second before repeating the loop
