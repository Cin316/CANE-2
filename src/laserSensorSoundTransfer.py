from src.laserSensor import *
import time
import threading

class LaserSensorSoundTransfer (threading.Thread):
    
    def __init__(self, soundThread, lasers, ids):
        self.soundThread = soundThread
        self.lasers = lasers
        self.ids = ids
    
    def run(self):
        while True:
            for laser, ID in zip(self.lasers, self.ids):
                self.soundThread.set_frequency(toFreq(laser.status()), ID)
            sleep(0.05)
    
    def toFreq(statusBool):
        if statusBool == True:
            return 0.2
        else:
            return 1.0e-6
