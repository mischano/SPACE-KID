from Window import Window
import Audio
import pygame

''' Set up & start playing the audio first to minimize audio input delay....'''
# Audio.setUpAudio()
# Audio.playAudio()   # menu music

wd = Window(1440, 820)
pygame.mixer_music.stop()
