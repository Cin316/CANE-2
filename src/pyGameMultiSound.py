from threading import Thread
from os import system
import time
import subprocess
import pygame
import commands


class PyGameSoundThread (Thread):
    # A class extending threading.Thread which plays a single sound file a
    # modifiable number of times per second.

    # is_robotting: True to continue working; False to safely end the thread
    
    # sounds: An array of sound objects containing a loaded WAV sound file to be played.
    # soundChannels: An array of pygame sound channel objects to play the sound.
    # delays: An array of the waiting periods between plays, calculated from the frequency
    # lastPlayTimes: An array of the last times it started playing the sound

    # blipLengths: An array of how long each sound should be played.  This is also the minimum time between sounds.

    def __init__(self, filenames):
        Thread.__init__(self)
        
	self.defaultBlipLength = 0.075
        
        pygame.init()
        
        self.sounds = []
        self.soundChannels = []
        self.lastPlayTimes = []
        self.delays = []
        self.blipLengths = []
        
        id = 1
        for filename in filenames:
            self.sounds.append(pygame.mixer.Sound(filename))
            self.soundChannels.append(pygame.mixer.Channel(id))
            id = id + 1
            self.lastPlayTimes.append(0)
            self.delays.append(10.0)
            self.blipLengths.append(self.defaultBlipLength)
        
        # Old stuff
        self.is_robotting = True

    def run(self):
        while self.is_robotting:
            for i in range(len(self.sounds)):
                if time.time() > self.lastPlayTimes[i] + self.blipLengths[i] + self.delays[i]:
                    #print("beep: " + str(i))
                    self.soundChannels[i].play(self.sounds[i])
	            self.lastPlayTimes[i] = time.time()
	        if time.time() > self.lastPlayTimes[i] + self.blipLengths[i]:
                    self.soundChannels[i].stop()
		
	    time.sleep(.001) 
	    
            
    def set_frequency(self, frequency, i):
        self.delays[i] = 1.0 / frequency
    
    # safely kill the thread
    def terminate(self):
        self.is_robotting = False
    

