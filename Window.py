import pygame
import sys
from pygame.locals import *
import Audio

''' RGB COLOR CODE '''
DARK_WHITE = (189, 176, 174)
BLACK = (0, 0, 0)
GREEN = (3, 156, 44)
RED = (163, 37, 11)
BRIGHT_DARK = (20, 20, 20)
GAME_TITLE = "SPACE KID"  # Title of the game. Shows on the top left corner.

''' MAIN MENU TEXT '''
MAIN_MENU_TEXT = {'t': (530, 20, 380, 100), 'p': (648, 250, 100, 55), 's': (606, 320, 180, 55), 'c': (619, 390, 160, 55),
             'e': (653, 460, 100, 55)}  # Title, play, settings, credits, exit.

'''CREDITS SUB-MENU TEXT'''
CREDITS_TEXT = {'c': (605, 180, 250, 80), 'a': (530, 330, 420, 40), 'm': (440, 380, 554, 45),
                'g': (580, 430, 280, 40), 't': (535, 520, 400, 35),
                'b': (30, 30, 130, 60)}

'''SETTINGS SUB-MENU TEXT'''
SETTINGS_TEXT = {'s': (573, 170, 260, 80), 'c': (620, 290, 190, 55), 'w': (585, 360, 255, 55), 'm': (619, 430, 180, 55),
                 'b': (30, 30, 130, 60)}


def exit_game():
    """ exit_game:
        Exit pygame & program.
    """
    pygame.quit()
    sys.exit()


def is_mouse_clicked():
    """ is_mouse_clicked:
        Check the status of the mouse.
        Return: True/False.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
            else:
                return False


class Window:
    def __init__(self, width, height):
        self.gameScreenWidth = width
        self.gameScreenHeight = height
        self.gameScreen = 0  # Menu window object.
        self.fontType = 'munro.ttf'

        self.playButton = 0
        self.settingsButton = 0
        self.creditsButton = 0
        self.exitButton = 0

        self.main_menu()

    def init_window(self):
        """ init_window:
            Create & initialize the window.
            Return: background image.
        """
        pygame.init()
        self.gameScreen = pygame.display.set_mode((self.gameScreenWidth, self.gameScreenHeight))  # Set the game window.
        pygame.display.set_caption(GAME_TITLE)  # Set the game caption (top left corner).
        get_image = pygame.image.load('background.jpg')  # Load the background image.
        return get_image

    def main_menu(self):
        """ main_menu:
            Displays main menu & sub-menus
            Calls exit_game() to exit the game.
        """
        background_image = self.init_window()

        while True:
            mx, my = pygame.mouse.get_pos()  # Mouse coordinates.
            self.gameScreen.blit(background_image, (0, 0))  # Render the background image.

            ''' Draw welcome letter & menu options.'''
            self.draw(100, MAIN_MENU_TEXT['t'], 'SPACE KID', RED)  # Game title.
            self.playButton = self.draw(55, MAIN_MENU_TEXT['p'], 'Play', DARK_WHITE)  # Play button.
            self.settingsButton = self.draw(55, MAIN_MENU_TEXT['s'], 'Settings', DARK_WHITE)  # Settings button.
            self.creditsButton = self.draw(55, MAIN_MENU_TEXT['c'], 'Credits', DARK_WHITE)  # Credits button.
            self.exitButton = self.draw(55, MAIN_MENU_TEXT['e'], 'Exit', DARK_WHITE)  # Exit button.

            ''''Check if the user clicked any of the menu options.'''
            self.is_menu_option_selected(is_mouse_clicked(), background_image, (mx, my))

            pygame.display.update()  # Update gameScreen.

    def is_menu_option_selected(self, click, image, mouse):
        """ is_menu_option_selected:
            Check if menu option clicked.
            Args:
                click (bool) - mouse status
                image (jpg) - background image
                mouse (x,y) - mouse position
        """
        if self.playButton.collidepoint(mouse):
            self.draw(55, MAIN_MENU_TEXT['p'], 'Play', RED)
            if click:
                pass
        if self.settingsButton.collidepoint(mouse):
            self.draw(55, MAIN_MENU_TEXT['s'], 'Settings', RED)
            if click:
                self.menu_settings(image)
        if self.creditsButton.collidepoint(mouse):
            self.draw(55, MAIN_MENU_TEXT['c'], 'Credits', RED)  # Highlight the text.
            if click:
                self.menu_credits(image)
        if self.exitButton.collidepoint(mouse):
            self.draw(55, MAIN_MENU_TEXT['e'], 'Exit', RED)
            if click:
                exit_game()

    def draw(self, font_size, rectangle, title, font_color):
        """ draw:
            Draw text inside the window.
            Args:
                font_size (int)
                rectangle - rectangle coordinates (refer to 'MENU OPTIONS')
                title (str) - text
                font_color - (refer to 'RGB Color Code')
            Return:
                 rect (x,y,z,k) - rectangle coordinates
        """
        pygame.font.init()
        font = pygame.font.Font(self.fontType, font_size)  # Load a custom font from
        rect = pygame.draw.rect(self.gameScreen, BRIGHT_DARK, rectangle)  # Draw a rectangle.
        text = font.render(title, 0, font_color)  # Render the text.
        # Note: text has to be blited over a geometric shape to be rendered.
        self.gameScreen.blit(text, rect)  # Render the text over a rectangle

        return rect

    def menu_credits(self, image):
        """ menu_credits:
            Display credits sub-menu.
            Args:
                image (jpg) - background image
        """

        go_back = False  # True when 'back' button is clicked.

        while not go_back:
            mouse = pygame.mouse.get_pos()

            self.gameScreen.blit(image, (0, 0))  # Display the image.

            '''Draw credits.'''
            self.draw(80, CREDITS_TEXT['c'], 'Credits', DARK_WHITE)
            self.draw(40, CREDITS_TEXT['a'], 'Author: Mansur Ischanov', DARK_WHITE)
            self.draw(40, CREDITS_TEXT['m'], 'Mail: mansur.ischanov@gmail.com:', DARK_WHITE)
            self.draw(40, CREDITS_TEXT['g'], 'Github: mischano', DARK_WHITE)
            self.draw(30, CREDITS_TEXT['t'], 'Big thanks to pygame creators! ', DARK_WHITE)
            back_button = self.draw(50, CREDITS_TEXT['b'], 'Back', DARK_WHITE)  # Back button.

            '''Highlight 'back' button.'''
            if back_button.collidepoint(mouse):
                self.draw(50, CREDITS_TEXT['b'], 'Back', RED)

            '''If 'back' button is clicked...'''
            if is_mouse_clicked() and back_button.collidepoint(mouse):
                self.draw(50, CREDITS_TEXT['b'], 'Back', RED)  # Highlight again before exiting.
                go_back = True

            pygame.display.update()

    def menu_settings(self, image):

        go_back = False

        while not go_back:
            mouse = pygame.mouse.get_pos()

            self.gameScreen.blit(image, (0, 0))

            '''Draw settings.'''
            self.draw(80, SETTINGS_TEXT['s'], 'Settings', DARK_WHITE)
            controls_button = self.draw(50, SETTINGS_TEXT['c'], 'Controls', DARK_WHITE)
            window_button = self.draw(50, SETTINGS_TEXT['w'], 'Window Size', DARK_WHITE)
            music_button = self.draw(50, SETTINGS_TEXT['m'], 'Music on', DARK_WHITE)
            back_button = self.draw(50, SETTINGS_TEXT['b'], 'Back', DARK_WHITE)

            if controls_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['c'], 'Controls', RED)
                if is_mouse_clicked():
                    self.menu_settings_controls(image)
            if window_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['w'], 'Window Size', RED)
            if music_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['m'], 'Music on', RED)
            if back_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['b'], 'Back', RED)

            '''If 'back' button is clicked...'''
            if is_mouse_clicked() and back_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['b'], 'Back', RED)  # Highlight again before exiting.
                go_back = True

            pygame.display.update()

    def menu_settings_controls(self, image):
        go_back = False
        while not go_back:
            mouse = pygame.mouse.get_pos()
            self.gameScreen.blit(image, (0, 0))

            self.draw(80, SETTINGS_TEXT['s'], 'Controls', DARK_WHITE)
            self.draw(50, SETTINGS_TEXT['w'], 'W', DARK_WHITE)
            self.draw(50, SETTINGS_TEXT['m'], 'S', DARK_WHITE)
            back_button = self.draw(50, SETTINGS_TEXT['b'], 'Back', DARK_WHITE)

            if back_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['b'], 'Back', RED)
            if is_mouse_clicked() and back_button.collidepoint(mouse):
                self.draw(50, SETTINGS_TEXT['b'], 'Back', RED)  # Highlight again before exiting.
                go_back = True
            pygame.display.update()
