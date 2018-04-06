from src.newUltrasonic import *
from src.pyGameMultiSound import *
from src.caneServer import *

sideOpt = DistanceOptions()
sideOpt.minDistance = 0.02
sideOpt.maxDistance = 1.0
sideOpt.inverseConstant = 0.7
frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

sound = PyGameSoundThread(["sound/98left.wav", "sound/884left.wav", "sound/884right.wav", "sound/98right.wav"]) # TODO This ordering is probably all mixed up.

sideLeftSM = ServerCommStateMachine()
frontLeftSM = ServerCommStateMachine()
frontRightSM = UltrasonicStateMachine(24, 4, frontOpt)
sideRightSM = UltrasonicStateMachine(24, 12, sideOpt)

server = CANEServer(sideLeftSM, frontLeftSM)
#server.start()

thread = UltrasonicThread([sideLeftSM, frontLeftSM, frontRightSM, sideRightSM],
                          [sound,      sound,       sound,        sound      ])

thread.start()
thread.join()
