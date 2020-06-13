import random
import os.path
import pygame


class Background:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.index = 0
        self.rand_num = 0

    def load_image(self, index):
        get_image = pygame.image.load(os.path.join('image', str(index) + '.jpg'))  # load the background image from .py dir.
        get_image = pygame.transform.scale(get_image, (self.width, self.height))
        return get_image

    def get_image(self):
        if self.index % 40 == 0:
            self.rand_num = random.randrange(0, 55, 1)
        image = self.load_image(self.rand_num)
        self.index += 1
        return image


