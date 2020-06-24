from display import Window
from background import Background
import pygame

# CLOCK = pygame.time.Clock()


class Menu(Window):
    """
    A class to represent main and sub-menus

    """

    def __init__(self, full_screen, fps):
        """
        :param full_screen:
            bool -- set to True if game is in full screen mode, False otherwise

        :param fps:
            int -- number of frames per second

        """
        super(Menu, self).__init__(1440, 820, full_screen, fps)
        super().init_window()

        self.fps = fps
        self.background_obj = Background(self.width, self.height)

    def main_menu(self):
        """ Calls main menu and sub-menus until 'Exit' or 'Play' buttons are clicked.

        :param: None

        :return: None
        """

        done = False    # false until a button is clicked
        while not done:
            self.screen.blit(self.background_obj.get_image(), (0, 0))   # get background image & blit it on the screen
            done = self.display()   # display drawings on the screen & check if any button is clicked

            pygame.display.update()     # update the screen

        self.main_menu()    # recursively call itself until 'Exit' or 'Play' buttons are clicked
