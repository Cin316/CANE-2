from threading import Thread
from os import system
import time
import subprocess
import math
import pyaudio
import numpy


class PySoundThread (Thread):
    # A class extending threading.Thread which plays a single sound file a
    # modifiable number of times per second.
    # t_last: the time at which the last sound started (system time, 
    #             not UTC-synchronized)
    # delay: the waiting period between plays, calculated from the frequency
    # is_robotting: True to continue working; False to safely end the thread
    # soundProcess: a Popen object that represents a pipe to the sox command
    
    # pyAudio: a PyAudio object
    # audioStream: a stream object that audio can be written to

    def __init__(self, filename):
        Thread.__init__(self)
        cmd = ["play", "-t", "u3", "-"]
        #self.soundProcess = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        
        self.samplingRate = 8000
        self.outputChunkSize = 800
        self.timeBetweenChunks = self.outputChunkSize/float(self.samplingRate)


        self.beepFrequency = 320
        self.recalcWaitTime()
	
        self.delay = 10.0
	
	self.blipLength = 0.075

        p = pyaudio.PyAudio()
        self.stream = p.open(format = p.get_format_from_width(2), # Each frame is 2 bytes long
                        channels = 1,
                        rate = self.samplingRate,
                        output = True)
        
        # Old stuff
        self.system_command = 'play -q ' + filename + ' pad 1 &'
        self.t_last = time.time()
        self.is_robotting = True

    # Goal: Output 800 frames every 0.1 seconds.

    def run(self):
	bufferStr = ''
        while self.is_robotting:
            self.recalcWaitTime()
            
            loopStartTime = time.time()
            
            newStr = ''
            
            loopCount = 0
            while loopCount < self.blipLength*self.samplingRate:
                newStr = newStr + ( chr(0xff)*self.intWaitTime )
                loopCount += self.intWaitTime
                newStr = newStr + ( chr(0x00)*self.intWaitTime )
                loopCount += self.intWaitTime
            
            newStr = newStr + ( chr(0x00)*int(self.delay*self.samplingRate) )
            
            bufferStr = bufferStr + newStr
            while len(bufferStr)>=self.outputChunkSize:
                outputStr = bufferStr[:self.outputChunkSize]
                bufferStr = bufferStr[self.outputChunkSize:]

                self.stream.write(outputStr)
                #self.soundProcess.stdin.write(byteArray)
                #self.soundProcess.stdin.flush()
                
                print("bufferStr length: " + str(len(bufferStr)))
                print("outputted " + str(len(outputStr)) + " bytes in " + str(time.time()-loopStartTime) + " | rate: " + str(len(outputStr)/(time.time()-loopStartTime)) + " bytes/s")
                loopStartTime = time.time()

    
    def recalcWaitTime(self):
	self.lengthOfOscillation = (1.0/self.beepFrequency)*self.samplingRate
	self.intWaitTime = int(self.lengthOfOscillation)
        

    def set_frequency(self, frequency):
        self.delay = 1.0 / frequency
    
    # safely kill the thread
    def terminate(self):
        self.is_robotting = False
