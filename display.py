import background
import render
import pygame
import status
import audio
import stack

''' RGB colors '''
DARK_WHITE = (189, 176, 174)    # menu text color
RED = (163, 1, 1)         # menu text highlight color

''' Game title '''
GAME_TITLE = "SPACE KID"  # Title of the game. Shows on the top left corner.


class Window:
    def __init__(self, width, height, fs, fps):
        self.width = width
        self.height = height
        self.screen = 0  # menu window object.
        self.full_screen = fs
        self.fps = fps

        self.i = 100

        self.stack_obj = stack.Stack()
        self.background_obj = background.Background(self.width, self.height)

    def init_window(self):
        """ init_window -- Creates & initialize a new window for the game.
        *
        *   INPUT: none
        *
        *   OUTPUT: none
        """

        pygame.init()

        ''' If bool full_screen is set to True, create a full-screen window, otherwise create 1440x820 window '''
        if not self.full_screen:
            screen = pygame.display.set_mode((self.width, self.height))

        else:
            screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

        ''' Window title. Appears on the top left corner '''
        pygame.display.set_caption(GAME_TITLE)
        return screen

    def display(self):
        """ display -- Calls helper methods to draw transparent rectangles & blit text over them, highlights text,
                        menu sound effects, checks if options are clicked/selected"""

        ''' Loop until user clicks/ a menu/sub-menu option '''

        done = False
        while not done:
            self.screen.blit(self.background_obj.get_image(), (0, 0))  # get background image & blit it on the screen

            '''Check if menu/sub-menu option is clicked. If button is 0 (back/exit button is clicked) break the loop, 
               let menu re-call itself to go back to previous menu '''
            button = status.is_button_clicked(self.stack_obj)
            if button == 0:
                break

            button_name = button[0]     # button text (str)
            button_font_size = button[2]    # button text size (int)
            num_of_button = len(button[0])  # number of buttons (int)
            drawn_button = [0] * num_of_button  # a list to contain drawn buttons
            rect_pos = button[1]        # rectangle position to blit the button text over
            click = status.is_mouse_clicked()  # status of the mouse (bool)
            # a range of text that can be highlighted & clicked.
            _min = button[3][0]
            _max = button[3][1]

            ''' Draw buttons on the screen '''
            for i in range(num_of_button):
                drawn_button[i] = render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i], DARK_WHITE)

            ''' Check if the mouse collides with any buttons '''
            for i in range(int(_min), int(_max)):

                ''' If mouse collides with a button, perform the followings bellow... '''
                if drawn_button[i].collidepoint(pygame.mouse.get_pos()):

                    ''' Make sound effect once '''
                    if self.i is not i:
                        audio.play_sound('hower')
                        self.i = i
                    ''' Highlight the button in red color '''
                    self.screen = self.init_window()
                    self.screen.blit(self.background_obj.get_image(),
                                     (0, 0))  # get background image & blit it on the screen
                    for delta in range(num_of_button):
                        if delta == i:
                            pass
                        else:
                            drawn_button[delta] = render.draw(self.screen, button_name[delta], rect_pos[delta], button_font_size[delta],
                                                          DARK_WHITE)
                    render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i] + 10, RED)

                    ''' If button is clicked, make sound effect & push index into the stack (index used to determine 
                        which button is clicked '''
                    if click:
                        audio.play_sound('click')
                        self.stack_obj.push(i)

                        ''' Fade out the screen for nicer visual effects '''
                        render.draw_fade(self.init_window(), self.background_obj.get_image(), self.full_screen)
                        break

            pygame.display.update()



