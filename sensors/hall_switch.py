# TODO: Add option parsing
# GPIO Pin


# Imports
import RPi.GPIO as GPIO
import time

# GPIO Setup
inputpin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputpin, GPIO.IN)


# TODO: Add logging to sucessful reads
# TODO: Return True when detected
# TODO: Add test function that displays on screen
# TODO: Put edge detection into a function

# Edge Detection

def detection:
	try:
		GPIO.wait_for_edge(inputpin, GPIO.FALLING)
		print "Falling Edge Detected"
		print GPIO.input(inputpin)
	except KeyboardInterrupt:
		GPIO.cleanup

GPIO.cleanup
