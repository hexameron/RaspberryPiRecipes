# Import the libraries that we need
import urllib
import simplejson
import time
import RPi.GPIO as GPIO

# Set-up the General Purpose Input-Ouput (GPIO) pins
GPIO.cleanup() # Start from scratch
GPIO.setmode(GPIO.BCM) # Set GPIO mode for the Pi
GPIO.setup(4, GPIO.OUT) # Set Pin 4 on the GPIO header to be an output

# Create a function that takes a Twitter handle (e.g. @Raspberry_Pi) as an argument and returns the most recent tweet containing that handle 
def Latest_Tweet_to_Twitter_Handle(twitter_handle): # Define the function and show the arguments
 Twitter_search_results = urllib.urlopen("http://search.twitter.com/search.json?q="+twitter_handle) # Get the results of a search on Twitter for tweets containing the given hand$
 result_list = simplejson.loads(Twitter_search_results.read()) # Load the results
 return result_list["results"][0]["text"] # Return the first result

# This loop will use the function above to get the latest tweet mentioning that handle and check if it contains certain words
while(True): # The loop will run forever
 Tweet=Latest_Tweet_to_Twitter_Handle("@Raspberry_Pi") # Use the function above to get the latest tweet mentioning the handle given as an argument      
 if "ON" in Tweet: # Check if tweet contains the word given in quotation marks
  print Tweet," - Switch ON","\n" # If it did contain the word then print out the tweet along with the message "Switch ON"
  RPi.GPIO.output(4,1) # and switch on the given GPIO pin
 if "OFF" in Tweet # Check if tweet contains the word given in quotation marks
  print Tweet," - Switch OFF","\n" # If it did contain the word then print out the tweet along with the message "Switch ON"
  RPi.GPIO.output(4,0) # and switch off the given GPIO pin
 time.sleep(2) # Wait for 2 seconds before repeating
