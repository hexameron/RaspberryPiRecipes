# First we need to import the libraries that we need

# Import the urllib library so that we can read data from webpages
import urllib

# Import the simplejson library so that we can decode the data that we have read from the webpage
import simplejson

# Import the time library so that we can make the program pause for a fixed amounr of time
import time

# Import the Raspberry Pi GPIO libraries that allow us to connect the Raspberry Pi to other physical devices via the General Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO

# Now we need to set-up the General Purpose Input-Ouput (GPIO) pins

# Clear the current set-up so that we can start from scratch
GPIO.cleanup() 

# Set up the GPIO library to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Set pin 7 on the GPIO header to be an output
GPIO.setup(7, GPIO.OUT)

# Next we need to create a function that takes a Twitter handle (e.g. @Raspberry_Pi) as an argument and returns the most recent tweet containing that handle 

# Here we define the function name and show the arguments
def Latest_Tweet_to_Twitter_Handle(twitter_handle): 
 
 # The first thing the function does is to get the results of a search on Twitter for tweets containing the given hand$
 Twitter_search_results = urllib.urlopen("http://search.twitter.com/search.json?q="+twitter_handle) 
 
 # We then need to decode the data that we got from the webpage to form a list of tweets 
 result_list = simplejson.loads(Twitter_search_results.read()) 
 
 # The function then returns the first result in the list
 return result_list["results"][0]["text"] 

# Now for the main body of the program - this loop will use the function above to get the latest tweet mentioning the given handle and check if it contains certain words

# We want to the loop to run forever
while(True): 
 
 # Use the function above to get the latest tweet mentioning the handle given as an argument    
 Tweet=Latest_Tweet_to_Twitter_Handle("@Raspberry_Pi")   
 
 # Check if tweet contains the word given in quotation marks
 if "ON" in Tweet: 
  
  # If it did contain the word then print out the tweet along with the message "Switch ON"
  print Tweet," - Switch ON","\n" 
  
  # Then switch on the given GPIO pin
  GPIO.output(7,GPIO.HIGH) 
 
 # Check if tweet contains the word given in quotation marks
 if "OFF" in Tweet 
 
  # If it did contain the word then print out the tweet along with the message "Switch OFF"
  print Tweet," - Switch OFF","\n" 
  
  # Then switch off the given GPIO pin
  GPIO.output(7,GPIO.LOW) 
 
 # Wait for 2 seconds before repeating
 time.sleep(2) 
