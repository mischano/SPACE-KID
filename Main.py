import Menu as menuClass
import Audio
import pygame
import pygame
from time import sleep
''' Set up & start playing the audio first to minimize audio input delay....'''
# Audio.setUpAudio()
# Audio.playAudio()   # menu music

menu = menuClass.Menu(1440, 820)
play = menu.main_menu()
if play is True:
    pygame.display.update()

# pygame.mixer_music.stop()
