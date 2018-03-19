import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(15, gpio.IN, pull_up_down=gpio.PUD_DOWN)

while True:
	value = gpio.input(15)
	print(value)
	
