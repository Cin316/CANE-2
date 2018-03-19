from src.newUltrasonic import *
from src.pyGameMultiSound import *

sideOpt = DistanceOptions()
sideOpt.minDistance = 0.02
sideOpt.maxDistance = 1.0
sideOpt.inverseConstant = 0.7
frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

sound = PyGameSoundThread(["sound/98left.wav", "sound/884left.wav"])

thread = UltrasonicThread([24,             24            ],
                          [12,             5             ],
                          [sideOpt,        frontOpt      ],
                          [sound,         sound         ])

thread.start()
thread.join()
