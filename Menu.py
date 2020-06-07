import Rectangle as rectangleClass
import pygame
import Window
from Window import GameWindow

CLOCK = pygame.time.Clock()


class GameMenu():

    def __init__(self, width, height):
        self.game_window = GameWindow(width, height)
        self.is_window_full_screen = False

    def main_menu(self):
        """ main_menu: Displays the main menu. """
        rect_class_menu = rectangleClass.main_menu_text
        functions_list = [0, self.play, self.menu_settings, self.menu_credits, Window.exit_game]
        background_image = self.game_window.init_window(self.is_window_full_screen)  # create window.

        play = False
        while not play:
            mouse_pos = pygame.mouse.get_pos()  # mouse coordinates.
            self.game_window.gameScreen.blit(background_image, (0, 0))  # render the background image.

            '''' Display menu options & check if any of the options is clicked .'''
            play = self.game_window.display(rect_class_menu, functions_list, mouse_pos, background_image)

            pygame.display.update()  # update gameScreen.
            CLOCK.tick(self.game_window.fps)
        return True

    def menu_credits(self, image):
        """ menu_credits: display credits sub-menu.
            args: image (jpg) - background image
        """
        rect_class_credits = rectangleClass.credits_text
        functions_list = [0]        # dummy list to satisfy display method parameter number.

        go_back = False  # True when 'back' button is clicked.
        while not go_back:
            mouse = pygame.mouse.get_pos()
            self.game_window.gameScreen.blit(image, (0, 0))  # Display the image.
            go_back = self.game_window.display(rect_class_credits, functions_list, mouse, image)
            pygame.display.update()
            CLOCK.tick(self.game_window.fps)

    def menu_settings(self, image):
        """ menu_settings: displays settings menu.
            args: image (jpg): background image
        """
        rect_class_settings = rectangleClass.settings_text
        functions_list = [0, self.menu_settings_graphics, self.menu_settings_controls, self.menu_settings_music]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()
            self.game_window.gameScreen.blit(image, (0, 0))
            go_back = self.game_window.display(rect_class_settings, functions_list, mouse_pos, image)
            pygame.display.update()
            CLOCK.tick(self.game_window.fps)

    def menu_settings_controls(self, image):

        rect_class_controls = rectangleClass.settings_controls_text
        functions_list = [0]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.game_window.gameScreen.blit(image, (0, 0))
            go_back = self.game_window.display(rect_class_controls, functions_list, mouse_pos, image)

            pygame.display.update()
            CLOCK.tick(self.game_window.fps)

    def menu_settings_graphics(self, image):
        """ menu_settings_graphics: displays graphics sub menu.
            args: image (jpg) background image
        """
        rect_class_graphics = rectangleClass.settings_graphics
        function_list = [0, self.menu_settings_graphics_screen_size, self.menu_settings_graphics_fps]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.game_window.gameScreen.blit(image, (0, 0))
            go_back = self.game_window.display(rect_class_graphics, function_list, mouse_pos, image)

            pygame.display.update()
            CLOCK.tick(self.game_window.fps)

    def menu_settings_graphics_screen_size(self, image):
        """ menu_settings_graphics_screen_size: display change screen size sub menu.
            args: image (jpg) - background image
        """
        rect_class_screen_size = rectangleClass.settings_graphics_window_size
        function_list = [0, self.full_screen, self.window_screen]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.game_window.gameScreen.blit(image, (0, 0))
            go_back = self.game_window.display(rect_class_screen_size, function_list, mouse_pos, image)
            pygame.display.update()
            CLOCK.tick(self.game_window.fps)

    def full_screen(self, image):
        """ full_scree: change to full screen.
            args: image (jpg) - background image
        """
        rec = self.game_window.init_window(True)
        return rec

    def window_screen(self, image):
        """ window_screen: change to window screen.
            args: image (jpg) - background image
        """
        rec = self.game_window.init_window(False)
        return rec

    def menu_settings_graphics_fps(self, image):
        """ menu_settings_graphics_fps: display fps submenu.
            args: image (jpg) - background image
        """
        rect_class_fps = rectangleClass.settings_graphics_fps
        function_list = [0, self.change_fps, self.change_fps]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.game_window.gameScreen.blit(image, (0, 0))
            go_back = self.game_window.display(rect_class_fps, function_list, mouse_pos, image)
            pygame.display.update()
            CLOCK.tick(self.game_window.fps)

    def change_fps(self, image):
        exit()

    def menu_settings_music(self, image):
        pass

    def play(self, image):
        exit()


