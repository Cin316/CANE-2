from threading import Thread
from os import system
import time
import subprocess
import pygame


class PyGameSoundThread (Thread):
    # A class extending threading.Thread which plays a single sound file a
    # modifiable number of times per second.
    # t_last: the time at which the last sound started (system time, 
    #             not UTC-synchronized)
    # delay: the waiting period between plays, calculated from the frequency
    # is_robotting: True to continue working; False to safely end the thread
    
    # sound: A sound object containing a loaded WAV sound file to be played.
    # soundChannel: A pygame sound channel object to play the sound.
    

    def __init__(self, filename):
        Thread.__init__(self)
        
        self.delay = 10.0
	
	self.blipLength = 0.075
        
        pygame.mixer.init(48000, -16, 1, 1024)
        
        self.sound = pygame.mixer.Sound(filename)
        self.soundChannel = pygame.mixer.Channel(1) # TODO resolve conflicts here.  Multiple threads can't have the same soundChannel ID.

        
        # Old stuff
        self.t_last = time.time()
        self.is_robotting = True

    # Goal: Output 800 frames every 0.1 seconds.

    def run(self):
	bufferStr = ''
        while self.is_robotting:
            self.soundChannel.play(self.sound)
            time.sleep(self.blipLength)
            self.soundChannel.stop()
            time.sleep(self.delay) # TODO Maybe use self.delay-self.blipLength ??

            
    def set_frequency(self, frequency):
        self.delay = 1.0 / frequency
    
    # safely kill the thread
    def terminate(self):
        self.is_robotting = False

