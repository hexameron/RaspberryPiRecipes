import urllib
import simplejson
import re
from termcolor import colored
from time import sleep
import RPi.GPIO as GPIO

gpio_pin = {"pink":22, "red":7, "green":26, "yellow":24}

morse_code = {'A':"-", 'B':"-...", 'C':"-.-.", 'D':"-..", 'E':".", 
            'F':"..-.", 'G':"--.", 'H':"....", 'I':"..", 'J':".---", 
            'K':"-.-", 'L':".-..", 'M':"--", 'N':"-.", 'O':"---",
            'P':".--.", 'Q':"--.-", 'R':".-.",  'S':"...", 'T':"-",
            'U':"..-", 'V':"...-", 'W':".--", 'X':"-..-",'Y':"-.--",
            'Z':"--.."}

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(gpio_pin["red"], GPIO.OUT)
GPIO.setup(gpio_pin["green"], GPIO.OUT)
GPIO.setup(gpio_pin["yellow"], GPIO.OUT)
GPIO.setup(gpio_pin["pink"], GPIO.OUT)

def encode(string_input):
  string_output=""
  string_input = re.sub('[^A-Za-z0-9]+', '', string_input)
  for letter in string_input:
    string_output += morse_code[letter.upper()]
  return string_output

def latest_tweet(twitter_handle):
 twitter_search_results = urllib.urlopen("http://search.twitter.com/search.json?q="+twitter_handle)
 result_list = simplejson.loads(twitter_search_results.read())
 return result_list["results"][0]["text"]

def flash_morse_code(color, morse_code):
  for i in morse_code:
    GPIO.output(gpio_pin[color], GPIO.HIGH)
    if i == '.':
      sleep(1)
    elif i == '-':     
      sleep(2)
    GPIO.output(gpio_pin[color], GPIO.LOW)
    sleep(1)

def output_color(color):
  if color in tweet.lower():
    morse_code = encode(tweet)
    flash_morse_code(color, morse_code)
    print colored(color.upper()+" LED:", color), tweet, "=>", morse_code, "\n"

while(True): 
 tweet=latest_tweet("BigBangPi")
 output_color("red")
 output_color("yellow")
 output_color("pink")
 output_color("green")
 sleep(1)