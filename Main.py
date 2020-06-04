from Window import Window
import Audio
import pygame
import pygame
from time import sleep
''' Set up & start playing the audio first to minimize audio input delay....'''
# Audio.setUpAudio()
# Audio.playAudio()   # menu music

wd = Window(1440, 820)
# wd = Window(900, 800)
play = wd.main_menu()
if play is True:
    pygame.display.update()

# pygame.mixer_music.stop()
