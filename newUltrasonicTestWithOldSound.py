from src.newUltrasonic import *
from src.sound import *

frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

leftFrontSound = SoxSoundThread("sound/884left.wav")

thread = UltrasonicThread([24],
                          [5],
                          [frontOpt],
                          [leftFrontSound])

thread.start()
thread.join()
