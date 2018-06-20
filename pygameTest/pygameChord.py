import pygame.mixer
from time import sleep

pygame.mixer.init(48000, -16, 1, 1024)

sndA = pygame.mixer.Sound("A.wav")
sndB = pygame.mixer.Sound("Cs.wav")
sndC = pygame.mixer.Sound("E.wav")

soundChannel1A = pygame.mixer.Channel(1)
soundChannel1B = pygame.mixer.Channel(2)
soundChannel1C = pygame.mixer.Channel(3)

print "Soundboard Ready."

waitTime = 0.01

while True:
    soundChannel1A.play(sndA)
    sleep(0.05)
    soundChannel1A.stop()
    sleep(waitTime)
    waitTime = waitTime + 0.01


