import pyaudio
import numpy as np

def gensin(frequency, duration, sampRate):

	cycles = np.linspace(0,duration*2.0*np.pi,num=duration*sampRate)
	wave = np.sin(cycles*frequency,dtype='float32')
	t = np.divide(cycles,2.0*np.pi)
	
	return t, wave

frequency=440.0	 #in Hz
duration=20.0		 #in HOURS LOL no it's seconds
sampRate=44100.0	 #in Hz

t, sinWav = gensin(frequency,duration,sampRate)

p = pyaudio.PyAudio()

stream = p.open(format = pyaudio.paInt32,
		channels = 1,
		rate = int(sampRate),
		output = True)

stream.start_stream()

stream.write(sinWav)

