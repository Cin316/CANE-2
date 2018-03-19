import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

# Setup BCM pin 3 (physical pin 5) as an input.
# Grouding this pin wakes the Pi; this script extends
# the functionality to shutting down. This pin
# has a permanent pull-up resistor
GPIO.setup(3, GPIO.IN)

while True:
	if GPIO.input(3):
		# Do nothing.
		pass
	else:
		os.system("sudo poweroff")
	time.sleep(0.1)
