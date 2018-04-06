from src.newUltrasonic import *
from src.pyGameMultiSound import *

frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

sound = PyGameSoundThread(["sound/884left.wav"])

thread = UltrasonicThread([24],
                          [5],
                          [frontOpt],
                          [sound])

thread.start()
thread.join()

