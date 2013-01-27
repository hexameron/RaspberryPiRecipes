# First we need to import the libraries that we need

# Import the time library so that we can make the program pause for a fixed amount of time
import time

# Import the Raspberry Pi GPIO libraries that allow us to connect the Raspberry Pi to other physical devices via the General Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO

# Now we need to set-up the General Purpose Input-Ouput (GPIO) pins

# Clear the current set-up so that we can start from scratch
GPIO.cleanup()

# Set up the GPIO library to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Set Pin 7 on the GPIO header to act as an output
GPIO.setup(7, GPIO.OUT)

# This loop runs forever and flashes the LED
while True:
       
  # Turn on the LED
GPIO.output(7,GPIO.HIGH)

       # Wait for a second
       time.sleep(1)

# Turn off the LED
GPIO.output(7,GPIO.LOW)

       # Wait for a second
       time.sleep(1)
