from display import Window
from background import Background
import audio
import pygame

# CLOCK = pygame.time.Clock()


class Menu(Window):

    def __init__(self, full_screen, fps):
        super(Menu, self).__init__(1440, 820, full_screen, fps)
        super().init_window()

        self.fps = fps
        # self.background_obj = Background(self.width, self.height)

        audio.load_music('Sofi.wav')
        audio.play_music()

    def main_menu(self):

        done = False    # false until a button is clicked
        '''while not done:
            self.screen.blit(self.background_obj.get_image(), (0, 0))   # get background image & blit it on the screen
            done = self.display()   # display drawings on the screen & check if any button is clicked

            pygame.display.update()     # update the screen'''
        self.display()

        self.main_menu()    # recursively call itself until 'Exit' or 'Play' buttons are clicked
