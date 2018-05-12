from src.newUltrasonic import *
from src.pyGameMultiSound import *
from src.caneServer import *
from src.laserSensor import *
from src.laserSensorSoundTransfer import *

sideOpt = DistanceOptions()
sideOpt.minDistance = 0.02
sideOpt.maxDistance = 1.0
sideOpt.inverseConstant = 0.7
frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

sound = PyGameSoundThread(["sound/98left.wav", "sound/884left.wav", "sound/884right.wav", "sound/98right.wav", "sound/dropoffRight.wav", "sound/dropoffLeft.wav"]) # TODO This ordering is probably all mixed up.

sound.blipLengths[4] = 2.0
sound.blipLengths[5] = 2.0

laser = LaserSensor()
dummyLaser = DummyLaserSensor()

laserTransfer = LaserSensorSoundTransfer(sound, [laser, dummyLaser], [4, 5])
laserTransfer.start()

sideLeftSM = ServerCommStateMachine()
frontLeftSM = ServerCommStateMachine()
frontRightSM = UltrasonicStateMachine(24, 5, frontOpt)
sideRightSM = UltrasonicStateMachine(24, 12, sideOpt)

server = CANEServer(sideLeftSM, frontLeftSM, dummyLaser)
server.start()

thread = UltrasonicThread([sideLeftSM, frontLeftSM, frontRightSM, sideRightSM],
                          [sound,      sound,       sound,        sound      ])

thread.start()
thread.join()

