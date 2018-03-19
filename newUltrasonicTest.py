from src.newUltrasonic import *
from src.newSound import *

sideOpt = DistanceOptions()
sideOpt.minDistance = 0.02
sideOpt.maxDistance = 1.0
sideOpt.inverseConstant = 0.7
frontOpt = DistanceOptions()
frontOpt.minDistance = 0.10
frontOpt.maxDistance = 3.5
frontOpt.inverseConstant = 1
frontOpt.frontSensor = True

leftSideSound = NewSoxSoundThread("sound/99left.wav")
leftSideSound.beepFrequency=98
leftFrontSound = NewSoxSoundThread("sound/884left.wav")
leftFrontSound.beepFrequency=884
rightFrontSound = NewSoxSoundThread("sound/884right.wav")
rightFrontSound.beepFrequency=884
rightSideSound = NewSoxSoundThread("sound/98right.wav")
rightSideSound.beepFrequency=98

thread = UltrasonicThread([24,             24            ],
                          [12,             5             ],
                          [sideOpt,        frontOpt      ],
                          [rightSideSound, rightFrontSound])

thread.start()
thread.join()
