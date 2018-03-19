import time
from src.ultrasonic import *
import RPi.GPIO as gpio

class TimeoutException(Exception):
	pass

frontSensor = UltrasonicSensor(24, 5, 0, 10.0, 0.1, 10)
sideSensor = UltrasonicSensor(24, 12, 0, 10.0, 0.1, 10)


while True:
	frontSensor.ping()
	frontSensor.find_distance()
	time.sleep(0.5)
	#sideSensor.ping()
	#sideSensor.find_distance()
	#time.sleep(0.5)

gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.OUT)

# 5 is the front sensor
# 12 is the side sensor
echoPin = 5

gpio.setup(echoPin, gpio.IN)

while True:
	try:
		gpio.output(24, 1)
		time.sleep(0.010)
		gpio.output(24, 0)
		
		echoWaitStart = time.time()
		while gpio.input(echoPin) == 0:
			if (time.time() - echoWaitStart > 1.0):
				raise TimeoutException
		startTime = time.time()
		while gpio.input(echoPin) == 1:
			None
		endTime = time.time()
		difference = endTime - startTime

		speedOfSound = 340.27 #Speed of sound in meters per second

		distanceInMeters = (difference * speedOfSound) / 2.0
		# divide by 2 because the time difference is the time it takes for sound to bounce there and back

		print("distance: " + str(distanceInMeters) + " m")

		time.sleep(0.3)

	except TimeoutException:
		print("Timed out!")


