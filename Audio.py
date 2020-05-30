import pygame


def setUpAudio():
    pygame.mixer.init()
    pygame.mixer_music.load('Sofi.mp3')


def playAudio():
    pygame.mixer_music.play()