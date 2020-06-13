from display import Window
from background import Background
import display
import rectangle
import pygame

CLOCK = pygame.time.Clock()


class Menu(Window):

    def __init__(self, fs, fps):

        super(Menu, self).__init__(1440, 820, fs, fps)  #
        self.fps = fps

        self.background_obj = Background(self.width, self.height)

    def main_menu(self):
        """ main_menu: displays the main menu. """

        rect_class_menu = rectangle.main_menu_text
        functions_list = [0, self.play, self.menu_settings, self.menu_credits, display.exit_game]

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
            CLOCK.tick(self.fps)

    def menu_credits(self, image):
        """ menu_credits: display credits sub-menu.
            args:
                image (jpg) - background image
        """
        rect_class_credits = rectangle.credits_text     # load rectangles properties to be drawn.
        functions_list = [0]        # dummy list to satisfy display method parameter number.

        go_back = False  # True when 'back' button is clicked.
        while not go_back:

            mouse = pygame.mouse.get_pos()      # get mouse coordinates.
            image = self.background_obj.get_image()     # get the next image to animate background.
            self.screen.blit(image, (0, 0))  # Render the background image to the screen.

            '''' Display credits sub-menu & check if 'back' button is clicked .'''
            go_back = super().display(rect_class_credits, functions_list, mouse, image)

            ''' Update screen. '''
            pygame.display.update()     # update screen.
            CLOCK.tick(self.fps)

    def menu_settings(self, image):
        """ menu_settings: displays settings menu.
            args: image (jpg): background image
        """
        rect_class_settings = rectangle.settings_text     # load rectangles properties to be drawn.

        # a list of callable methods inside the settings sub-menu.
        functions_list = [0, self.menu_settings_graphics, self.menu_settings_controls, self.menu_settings_music]

        go_back = False     # True when 'back' button is clicked.
        while not go_back:

            mouse_pos = pygame.mouse.get_pos()      # get mouse coordinates.
            image = self.background_obj.get_image()     # get the next image to animate background.
            self.screen.blit(image, (0, 0))     # render the background image to the screen.

            ''' Display settings sub-menu & check if any of the options is clicked. '''
            go_back = super().display(rect_class_settings, functions_list, mouse_pos, image)

            ''' Update screen. '''
            pygame.display.update()
            CLOCK.tick(self.fps)

    def menu_settings_controls(self, image):
        """ UNFINISHED. """
        rect_class_controls = rectangle.settings_controls_text
        functions_list = [0]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(image, (0, 0))
            go_back = super().display(rect_class_controls, functions_list, mouse_pos, image)

            pygame.display.update()
            CLOCK.tick(self.fps)

    def menu_settings_graphics(self, image):
        """ menu_settings_graphics: displays graphics sub menu.
            args:
                image (jpg) - background image
        """
        rect_class_graphics = rectangle.settings_graphics   # load rectangles properties that needs to be drawn.
        # a list of callable methods.
        function_list = [0, self.menu_settings_graphics_screen_size, self.menu_settings_graphics_fps]

        go_back = False     # True when 'back' button is clicked.
        while not go_back:

            mouse_pos = pygame.mouse.get_pos()  # get mouse coordinates.
            image = self.background_obj.get_image()  # get the next image to animate background.
            self.screen.blit(image, (0, 0))  # render the background image to the screen.

            ''' Display settings sub-menu & check if any of the options is clicked. '''
            go_back = super().display(rect_class_graphics, function_list, mouse_pos, image)

            ''' Update screen. '''
            pygame.display.update()
            CLOCK.tick(self.fps)

    def menu_settings_graphics_screen_size(self, image):
        """ menu_settings_graphics_screen_size: display change screen size sub-menu.
            args:
                image (jpg) - background image
        """
        # load rectangles properties that needs to be drawn.
        rect_class_screen_size = rectangle.settings_graphics_window_size
        function_list = [0, self.full_screen, self.window_screen]   # a list of callable methods.

        go_back = False     # True when 'back' button is clicked.
        while not go_back:

            mouse_pos = pygame.mouse.get_pos()  # get mouse coordinates.
            image = self.background_obj.get_image()  # get the next image to animate background.
            self.screen.blit(image, (0, 0))     # get the next image to animate background

            ''' Display settings sub-menu & check if any of the options is clicked. '''
            go_back = super().display(rect_class_screen_size, function_list, mouse_pos, image)

            ''' Update screen. '''
            pygame.display.update()
            CLOCK.tick(self.fps)

    def full_screen(self, image):
        """ full_scree: change the window to full screen mode.
            args:
                image (jpg) - background image
        """
        self.screen_size = True     # change to full screen (class Window).
        rec = super().init_window()     # re-initialize the window.
        return rec

    def window_screen(self, image):
        """ window_screen: change the window to window screen mode.
            args: image (jpg) - background image
        """
        self.screen_size = False    # change to window screen.
        rec = super().init_window()     # re-initialize the window.
        return rec

    def menu_settings_graphics_fps(self, image):
        """ menu_settings_graphics_fps: display fps submenu.
            args: image (jpg) - background image
        """
        rect_class_fps = rectangle.settings_graphics_fps
        function_list = [0, self.change_fps, self.change_fps]

        go_back = False
        while not go_back:
            mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(image, (0, 0))
            go_back = super().display(rect_class_fps, function_list, mouse_pos, image)
            pygame.display.update()
            CLOCK.tick(self.fps)

    def change_fps(self, image):
        exit()

    def menu_settings_music(self, image):
        pass

    def play(self, image):
        pass



