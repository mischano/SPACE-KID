import pygame
from pygame.locals import *
import sys
import Rectangle as rectangleClass

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


class Menu:

    def __init__(self, width, height):
        self.gameScreenWidth = width
        self.gameScreenHeight = height
        self.gameScreen = 0  # menu window object.
        self.fontType = 'munro.ttf'

        # self.main_menu()

    def init_window(self):
        """ init_window: Create & initialize a window.
            return: background image.
        """
        pygame.init()
        self.gameScreen = pygame.display.set_mode((self.gameScreenWidth, self.gameScreenHeight))  # set the game window.
        pygame.display.set_caption(GAME_TITLE)  # set the game caption (top left corner).
        get_image = pygame.image.load('background.jpg')  # load the background image from .py dir.
        return get_image

    def draw_render_blit(self, text, text_pos, font_size, font_color):
        """ draw_render_blit: Draws a rectangle, renders a text, & blits over a rectangle.
            args:
                text (str): string text
                text_pos (tuple): rectangle coordinates
                font_size (int): size of the font
                font_color (tuple): RGB color
            return:
                rectangle (tuple) - rectangle coordinates
        """
        pygame.font.init()
        font = pygame.font.Font(self.fontType, font_size)  # load a custom font from .py dir
        rect = pygame.draw.rect(self.gameScreen, BRIGHT_DARK, text_pos)  # draw_render_blit a rectangle.
        render_text = font.render(text, 0, font_color)  # render the text.
        ''' Note: text has to be blited over a geometric shape to be rendered. '''
        self.gameScreen.blit(render_text, rect)  # render the text over a rectangle

        return rect

    def display(self, rect_list, functions_list, mouse_pos, image):
        """ display: Check if any of the menu options clicked & display it if it is.
            args:
                rect_list (list): 2D array from Rectangle class
                functions_list (list): a list of functions to be called
                mouse_pos (x,y): mouse position
                image (jpg): background image
        """
        ''' A range of callable methods. '''
        min_range = rect_list[3][0]     # a range of text that can be highlighted & clicked.
        max_range = rect_list[3][1]
        back_button = max_range - 1

        text_len = len(rect_list[0])
        captured_text = [0] * text_len      # a list for collidable objects inside the window.
        click = is_mouse_clicked()          # mouse status.

        ''' Create rectangles objects & blit texts over them. '''
        for i in range(text_len):
            captured_text[i] = self.draw_render_blit(rect_list[0][i], rect_list[1][i], rect_list[2][i], DARK_WHITE)

        ''' Check for mouse collision & iteration with objects. '''
        for i in range(min_range, max_range):
            if captured_text[i].collidepoint(mouse_pos):        # if mouse hover over an object.
                self.draw_render_blit(rect_list[0][i], rect_list[1][i], rect_list[2][i], RED)   # highlight it in red.
                ''' If mouse is clicked, check what object it clicked if any. '''
                if click:
                    if i == back_button:      # if 'back' button clicked (last element in a list).
                        return True             # return true to exit calling loop.
                    else:
                        functions_list[i](image)    # refer to the last list of 2D list in Rectangle class.
        return False

    def main_menu(self):
        """ main_menu: Displays the main menu. """
        rect_class = rectangleClass.main_menu_text
        functions_list = [0, self.play, self.menu_settings, self.menu_credits, exit_game]
        background_image = self.init_window()  # create window.

        play = False
        while not play:
            mouse_pos = pygame.mouse.get_pos()  # mouse coordinates.
            self.gameScreen.blit(background_image, (0, 0))  # render the background image.

            '''' Display menu options & check if any of the options is clicked .'''
            play = self.display(rect_class, functions_list, mouse_pos, background_image)

            pygame.display.update()  # update gameScreen.

        return True

    def menu_credits(self, image):
        """ menu_credits: display credits sub-menu.
            args: image (jpg) - background image
        """
        rect_class = rectangleClass.credits_text
        functions_list = [0]        # dummy list to satisfy display method parameter number.

        go_back = False  # True when 'back' button is clicked.
        while not go_back:
            mouse = pygame.mouse.get_pos()
            self.gameScreen.blit(image, (0, 0))  # Display the image.
            go_back = self.display(rect_class, functions_list, mouse, image)
            pygame.display.update()

    def menu_settings(self, image):
        """ menu_settings: displays settings menu.
            args: image (jpg): background image
        """
        rect_class = rectangleClass.settings_text
        functions_list = [0, self.menu_settings_graphics, self.menu_settings_controls, self.menu_settings_music, self.re_init_window]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()
            self.gameScreen.blit(image, (0, 0))
            go_back = self.display(rect_class, functions_list, mouse_pos, image)
            pygame.display.update()

    def menu_settings_controls(self, image):

        rect_class = rectangleClass.settings_controls_text
        functions_list = [0]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.gameScreen.blit(image, (0, 0))
            go_back = self.display(rect_class, functions_list, mouse_pos, image)

            pygame.display.update()

    def menu_settings_graphics(self, image):
        rect_class = rectangleClass.settings_controls_window_size_text
        function_list = [0, self.re_init_window, self.re_init_window, self.re_init_window, self.re_init_window]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.gameScreen.blit(image, (0, 0))
            go_back = self.display(rect_class, function_list, mouse_pos, image)

            pygame.display.update()

    def re_init_window(self, image):
        pass

    def menu_settings_music(self, image):
        pass

    def play(self, image):
        pass
