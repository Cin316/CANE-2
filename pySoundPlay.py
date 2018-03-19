import pyaudio
import wave
import sys

CHUNK = 96000
#CHUNK = 999999999999999999999999999999999999999

#wf = wave.open('/usr/share/sounds/alsa/Front_Center.wav', 'rb')
wf = wave.open('20second_sine.wav', 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
print("framerate: " + str(wf.getframerate()))
data = wf.readframes(CHUNK)

while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.start_stream()

stream.stop_stream()
stream.close()

p.terminate()

