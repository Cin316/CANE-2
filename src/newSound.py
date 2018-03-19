from threading import Thread
from os import system
import time
import subprocess

class NewSoxSoundThread (Thread):
    # A class extending threading.Thread which plays a single sound file a
    # modifiable number of times per second.
    # t_last: the time at which the last sound started (system time, 
    #             not UTC-synchronized)
    # delay: the waiting period between plays, calculated from the frequency
    # is_robotting: True to continue working; False to safely end the thread
    # soundProcess: a Popen object that represents a pipe to the sox command
    
    def __init__(self, filename):
        Thread.__init__(self)
        cmd = ["play", "-t", "u3", "-"]
        self.soundProcess = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        
        self.samplingRate = 8000
        self.outputChunkSize = 800
        self.timeBetweenChunks = self.outputChunkSize/float(self.samplingRate)


        self.beepFrequency = 320
        self.recalcWaitTime()
	
        self.delay = 10.0
	
	self.blipLength = 0.075

        # Old stuff
        self.system_command = 'play -q ' + filename + ' pad 1 &'
        self.t_last = time.time()
        self.is_robotting = True

    # Goal: Output 800 frames every 0.1 seconds.

    def run(self):
	byteBuffer = []
        while self.is_robotting:
            self.recalcWaitTime()
            
            loopStartTime = time.time()
            
            newBytes = []
            
            loopCount = 0
            while loopCount < self.blipLength*self.samplingRate:
                newBytes = newBytes + ( [0xff]*self.intWaitTime )
                loopCount += self.intWaitTime
                newBytes = newBytes + ( [0x00]*self.intWaitTime )
                loopCount += self.intWaitTime
            
            newBytes = newBytes + ( [0x00]*int(self.delay*self.samplingRate) )
            
            byteBuffer = byteBuffer + newBytes
            while len(byteBuffer)>=self.outputChunkSize:
                outputBytes = byteBuffer[:self.outputChunkSize]
                byteBuffer = byteBuffer[self.outputChunkSize:]

                byteArray = bytearray(outputBytes)
                self.soundProcess.stdin.write(byteArray)
                self.soundProcess.stdin.flush()
                
                print("byteBuffer length: " + str(len(byteBuffer)))
                # Wait now
                while time.time() < loopStartTime + self.timeBetweenChunks:
                    pass
                print("outputted " + str(len(outputBytes)) + " bytes in " + str(time.time()-loopStartTime) + " | rate: " + str(len(outputBytes)/(time.time()-loopStartTime)) + " bytes/s")
                loopStartTime = time.time()

    
    def recalcWaitTime(self):
	self.lengthOfOscillation = (1.0/self.beepFrequency)*self.samplingRate
	self.intWaitTime = int(self.lengthOfOscillation)
        

    def set_frequency(self, frequency):
        self.delay = 1.0 / frequency
    
    # safely kill the thread
    def terminate(self):
        self.is_robotting = False
