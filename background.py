import random
import os.path
import pygame


class Background:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.image = self.load_image()

    def load_image(self):
        get_image = pygame.image.load(os.path.join('image', '99.png'))
        get_image = pygame.transform.scale(get_image, (self.width, self.height))
        return get_image

    def get_image(self):
        return self.image


