#!/usr/bin/python

###########
# Imports #
###########
import pygame
import time
from RPi import GPIO
from array import array
from pygame.locals import *

##############
# GPIO Setup #
##############
pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#########
# Setup #
#########
pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
tone_obj = ToneSound(frequency = 800, volume = .5)
DOT = "."
DASH = "-"
key_down_time=0
key_down_length=0

class ToneSound(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(pygame.mixer.get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
        for time in xrange(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples

def wait_for_keydown(pin):
    while GPIO.input(pin):
        time.sleep(0.01)

def wait_for_keyup(pin):
    while not GPIO.input(pin):
        time.sleep(0.01)
		
		


##################################
# Plays test tone upon execution #
##################################
tone_obj.play(-1) #the -1 means to loop the sound
time.sleep(2)
tone_obj.stop()

print("Ready")

###########################
# Contact Key Screen Test #
########################### 
# while True:
	# reading = GPIO.input(pin)
	# print("HIGH" if reading else "LOW")
	# time.sleep(1)

#########################
# Tone on Button Press: #
#     Pull Up Wiring    #
#########################
# while True:
	# wait_for_keydown(pin)
	# tone_obj.play(-1) 		# -1 means to loop the sound 
	# wait_for_keyup(pin)
	# tone_obj.stop()
	
################################
# Display Morse and Play Tone: #
#     Pull Up Wiring           #
################################
while True:
    wait_for_keydown(pin)
	key_down_time = time.time() # record the time when the key went down
    tone_obj.play(-1)           # -1 means to loop the sound
    wait_for_keyup(pin)
    key_down_length = time.time() - key_down_time 
    tone_obj.stop()
    
    if key_down_length > 0.15:
        print(DASH)
    else:
        print(DOT)