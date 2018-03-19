from src.sound import *

thd = SoxSoundThread("sound/884left.wav")

thd.start()

thd.set_frequency(1)

