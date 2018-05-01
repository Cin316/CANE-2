import RPi.GPIO as GPIO

class LaserSensor:
    
    dropoffPin = 15
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.dropoffPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    def status(self):
        if GPIO.input(self.dropoffPin)==1:
            return True
        else:
            return False
    


class DummyLaserSensor:

    def __init__(self):
        self.value = False
    
    def status(self):
        return self.value


