from window import Window
from background import Background
import properties
import pygame
import window


class Character(Window):
    def __init__(self, obj_menu):
        super(Character, self).__init__(1440, 820, obj_menu.screen_size, obj_menu.fps)
        self.fs = obj_menu.screen_size
        self.fps = obj_menu.fps
        self.background_obj = Background(obj_menu.width, obj_menu.height)

    def main_menu(self):
        """ main_menu: Displays the main menu. """
        rect_class_menu = properties.main_menu_text
        functions_list = [0, self.play, self.menu_settings, self.menu_credits, window.exit_game]

        super().init_window()

        play = False        # False until user clicks play button.
        while not play:
            mouse_pos = pygame.mouse.get_pos()  # mouse coordinates.
            image = self.background_obj.get_image()     # get the next image to animate background.
            self.screen.blit(image, (0, 0))  # render the background image to the screen.

            '''' Display menu options & check if any of the options is clicked .'''
            play = super().display(rect_class_menu, functions_list, mouse_pos, image)

            ''' Update screen. '''
            pygame.display.update()  # update screen.
            # CLOCK.tick(self.fps)

    def play(self):
        pass

    def menu_settings(self):
        pass

    def menu_credits(self):
        pass
