from window import Display
import audio

# CLOCK = pygame.time.Clock()


class Menu(Display):

    def __init__(self, full_screen, fps):
        super(Menu, self).__init__(1440, 820, full_screen, fps)

        self.screen = super().init_window()
        self.fps = fps

        audio.load_music('sofi.wav')
        audio.play_music()

        self.main_menu()

    def main_menu(self):

        self.display()
        self.main_menu()    # recursively call itself until 'Exit' or 'Play' buttons are clicked


start_obj = Menu(False, 120)
