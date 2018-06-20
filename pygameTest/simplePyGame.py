import pygame
import pygame.mixer
import time

#pygame.mixer.init(48000, -16, 1, 1024)
pygame.init()

sndA = pygame.mixer.Sound("A.wav")

soundChannel1A = pygame.mixer.Channel(1)

soundChannel1A.play(sndA)

time.sleep(5)

