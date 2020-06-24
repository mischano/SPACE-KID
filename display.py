import rectangle as rect
from stack import Stack
import render
import pygame
from pygame.locals import *
import sys

''' RGB COLOR CODE '''
DARK_WHITE = (189, 176, 174)
BLACK = (0, 0, 0)
GREEN = (3, 156, 44)
RED = (163, 37, 11)
BRIGHT_DARK = (20, 20, 20)
GAME_TITLE = "SPACE KID"  # Title of the game. Shows on the top left corner.


def exit_game(image):
    """ exit_game: Exit pygame & program. """
    pygame.quit()
    sys.exit()


def is_mouse_clicked():
    """ is_mouse_clicked: Check the status of the mouse.
        return: True/False. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game(event)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
            else:
                return False


class Window:
    def __init__(self, width, height, fs, fps):
        self.width = width
        self.height = height
        self.screen = 0  # menu window object.
        self.screen_size = fs
        self.fps = fps
        self.stack_obj = Stack()

    def init_window(self):
        """ init_window: Create & initialize a window.
            return: background image.
        """
        pygame.init()
        if not self.screen_size:
            self.screen = pygame.display.set_mode((self.width, self.height))  # set the game window.
        else:
            self.screen = pygame.display.set_mode((self.width, self.height), FULLSCREEN)  # set the game window.

        pygame.display.set_caption(GAME_TITLE)  # set the game caption (top left corner).

    def is_button_clicked(self):
        if self.stack_obj.size() != 0:
            if self.stack_obj.peek() != 0:
                button = rect.get_surface(self.stack_obj.size())[self.stack_obj.peek()]
            else:
                self.stack_obj.pop()
                return 0
        else:
            button = rect.get_surface(0)

        return button

    def display(self):

        button = self.is_button_clicked()
        if button == 0:
            return True

        button_name = button[0]
        button_font_size = button[2]
        num_of_button = len(button[0])
        drawn_button = [0] * num_of_button
        rect_pos = button[1]
        _min = button[3][0]  # a range of text that can be highlighted & clicked.
        _max = button[3][1]
        click = is_mouse_clicked()

        for i in range(num_of_button):
            drawn_button[i] = render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i], DARK_WHITE)
        for i in range(int(_min), int(_max)):
            if drawn_button[i].collidepoint(pygame.mouse.get_pos()):
                render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i], RED)
                if click:
                    self.stack_obj.push(i)
                    return True


