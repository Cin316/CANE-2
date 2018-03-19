from threading import Thread
from os import system
import time
import subprocess
import pygame


class PyGameSoundThread (Thread):
    # A class extending threading.Thread which plays a single sound file a
    # modifiable number of times per second.

    # is_robotting: True to continue working; False to safely end the thread
    
    # sounds: An array of sound objects containing a loaded WAV sound file to be played.
    # soundChannels: An array of pygame sound channel objects to play the sound.
    # delays: An array of the waiting periods between plays, calculated from the frequency
    # lastPlayTimes: An array of the last times it started playing the sound

    def __init__(self, filenames):
        Thread.__init__(self)
        
	self.blipLength = 0.075
        
        pygame.mixer.init(48000, -16, 1, 1024)
        
        self.sounds = []
        self.soundChannels = []
        self.lastPlayTimes = []
        self.delays = []
        
        id = 1
        for filename in filenames:
            self.sounds.append(pygame.mixer.Sound(filename))
            self.soundChannels.append(pygame.mixer.Channel(id))
            id = id + 1
            self.lastPlayTimes.append(0)
            self.delays.append(10.0)
        
        # Old stuff
        self.is_robotting = True

    def run(self):
        while self.is_robotting:
            for i in range(len(self.sounds)):
                if time.time() > self.lastPlayTimes[i] + self.blipLength + self.delays[i]:
                    self.soundChannels[i].play(self.sounds[i])
	            self.lastPlayTimes[i] = time.time()
	        if time.time() > self.lastPlayTimes[i] + self.blipLength:
                    self.soundChannels[i].stop()
		
	    time.sleep(.001) 
	    
            
    def set_frequency(self, frequency, i):
        self.delays[i] = 1.0 / frequency
    
    # safely kill the thread
    def terminate(self):
        self.is_robotting = False

