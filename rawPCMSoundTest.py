import time
from os import system
import subprocess
import sys

# u2 indicates unsigned 2-byte integer PCM
# it defaults to 8 kHz
cmd = ["play", "-t", "u3", "-"]
#cmd = ["tee", "pythonBlip.us"]

sox = subprocess.Popen(cmd, stdin=subprocess.PIPE)


samplingRate = 8000

beepFrequency = 320
lengthOfOscillation = (1.0/beepFrequency)*samplingRate
intWaitTime = int(lengthOfOscillation)

secondsBetweenBlips = 0.3

blipLength = 0.075

loopStartTime = time.time()
totalFramesOutputted = 0

while True:

	byteList = []
	lengthOfOscillation = (1.0/beepFrequency)*samplingRate
	intWaitTime = int(lengthOfOscillation)

	loopCount = 0
	while loopCount < blipLength*samplingRate:
		byteList = byteList + ( [0xff]*intWaitTime )
		loopCount += intWaitTime
		byteList = byteList + ( [0x00]*intWaitTime )
		loopCount += intWaitTime

	byteList = byteList + ( [0x00]*int(secondsBetweenBlips*samplingRate) )
	totalFramesOutputted += len(byteList)
	
	byteArray = bytearray(byteList)
	sox.stdin.write(byteArray)
	sox.stdin.flush()

	finishTime = loopStartTime + totalFramesOutputted/float(2*samplingRate)
	wakeTime = finishTime - 0.1
	print("diff: " + str(wakeTime - time.time()))
	
	while time.time() < wakeTime:
		pass

	if time.time() > loopStartTime + 5:
		secondsBetweenBlips = 0.6

	
