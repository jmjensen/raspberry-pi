# TODO: Add option parsing
# GPIO Pin
# Read Quantity
# Switch between interrupt and sleep
# Sleep duration

# Investigate pullup resistor

# Imports
import RPi.GPIO as GPIO
import time

# GPIO Setup
inputpin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputpin, GPIO.IN)

# Test
#for i in range(1000):
    #if GPIO.input(inputpin):
        ##print "."
        #print GPIO.input(inputpin)
    #else:
        ##print "touching!"
        #print GPIO.input(inputpin)
    #time.sleep(.01)
	# TODO: Add an interrupt to avoid getting signal while CPU processing earlier one
	# TODO: Add logging to sucessful reads

# Edge Detection
try:
 	GPIO.wait_for_edge(inputpin, GPIO.FALLING)
 	print "Falling Edge Detected"
 	print GPIO.input(inputpin)
except KeyboardInterrupt:
	GPIO.cleanup

GPIO.cleanup
