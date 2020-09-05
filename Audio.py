import pygame
import os


pygame.mixer.init()
channels = pygame.mixer.get_num_channels()

# music = {"menu": pygame.mixer.Sound('sound/Sofi.wav')}

sound = {"hower": pygame.mixer.Sound('sound/button_hower_01.wav'),
         "click": pygame.mixer.Sound('sound/button_click_01.wav')}


def play_sound(sound_name, ch=None):

    if ch is None:
        sound[sound_name].play()
    else:
        channel = pygame.mixer.Channel(ch)
        channel.stop()
        channel.play(sound[sound_name])


def load_music(music_name):
    pygame.mixer.music.load(os.path.join('sound', music_name))


def play_music():
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


