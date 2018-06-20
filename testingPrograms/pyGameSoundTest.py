from src.pyGameMultiSound import *

sound = PyGameSoundThread(["sound/dropoff.wav"])
sound.blipLengths[0] = 2.0

sound.start()

sound.set_frequency(0.4, 0)

sound.join()

