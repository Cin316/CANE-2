import time
import RPi.GPIO as gpio


gpio.setmode(gpio.BCM)

pins = [3, 15, 5, 12]
# 3 is power switch
# 15 is the laser sensor output
# 5 is the front ultrasonic sensor return
# 12 is the side ultrasonic sensor return

gpio.setup(3, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(15, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(5, gpio.IN)
gpio.setup(12, gpio.IN)

while True:
	for pin in pins:
		print(str(pin) + ": " + str(gpio.input(pin)))
	print("")
	time.sleep(0.1)
