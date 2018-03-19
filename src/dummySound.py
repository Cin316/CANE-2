from threading import Thread
from os import system
import time
import subprocess


class DummySoundThread (Thread):
    # A class to receive and store blipFrequencies.

    # is_robotting: True to continue working; False to safely end the thread
    # frequencies: An array of sound frequencies.
    
    def __init__(self, numberOfFreq):
        Thread.__init__(self)
        
        self.frequencies = [0.0]*numberOfFreq
        self.is_robotting = True

    def run(self):
	pass 
            
    def set_frequency(self, frequency, i):
        self.frequencies[i] = frequency
    
    # safely kill the thread
    def terminate(self):
        self.is_robotting = False

