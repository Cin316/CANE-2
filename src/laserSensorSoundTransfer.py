import time
from threading import Thread

class LaserSensorSoundTransfer (Thread):
    
    def __init__(self, soundThread, lasers, ids):
        Thread.__init__(self)
        self.soundThread = soundThread
        self.lasers = lasers
        self.ids = ids
    
    def run(self):
        while True:
            for laser, ID in zip(self.lasers, self.ids):
                self.soundThread.set_frequency(self.toFreq(laser.status()), ID)
            time.sleep(0.05)
    
    def toFreq(self, statusBool):
        if statusBool == True:
            return 1/2.5
        else:
            return 1.0e-6
