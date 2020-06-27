import background
import properties
import render
import pygame
import stack
import audio
import sys
from pygame.locals import *

''' RGB colors '''
DARK_WHITE = (189, 176, 174)    # menu text color
RED = (163, 37, 11)         # menu text highlight color

''' Game title '''
GAME_TITLE = "SPACE KID"  # Title of the game. Shows on the top left corner.


def exit_game():
    """ exit_game: Exit pygame & program. """
    pygame.quit()
    sys.exit()


def is_mouse_clicked():
    """ is_mouse_clicked -- Checks the status of the mouse.
    *
    *   INPUT: none
    *
    *    OUTPUT: True -- if mouse clicked
    *            Flase -- if mouse not clicked
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
            self.screen = pygame.display.set_mode((self.width, self.height))

        else:
            self.screen = pygame.display.set_mode((self.width, self.height), FULLSCREEN)

        ''' Window title. Appears on the top left corner '''
        pygame.display.set_caption(GAME_TITLE)

    def is_button_clicked(self):
        """ is_button_clicked -- Checks if any of the menu buttons are clicked.
        *
        *   INPUT: none
        *
        *   OUTPUT: button -- 2D list - containing text & rectangle properties to be drawn
        """

        # If variable is not initialized: Local variable 'button' might be referenced before assignment - warning occurs
        button = None

        ''' If stack size is 0, return main menu button properties '''
        if self.stack_obj.size() == 0:
            button = properties.get_properties(0)

        else:
            ''' If the top value of the stack is (0), back/exit button is clicked '''
            if self.stack_obj.peek() == 0:

                ''' If the stack size is 1, Exit button is clicked. Call exit method & exit the menu '''
                if self.stack_obj.size() == 1:
                    exit_game()

                else:
                    ''' Else, (back button is clicked) pop the last 2 values (refer to stack class for more information) 
                        & return (0) to be handled in display method '''
                    self.stack_obj.pop()
                    return 0
            else:
                ''' If the top value of the stack is not (0), load the sub-menu properties of the clicked button 
                    according to stack values & size '''
                button = properties.get_properties(self.stack_obj.size())[self.stack_obj.peek()]

        return button

    def display(self):
        """ display -- Calls helper methods to draw transparent rectangles & blit text over them, highlights text,
                        menu sound effects, checks if options are clicked/selected"""

        ''' Loop until user clicks/ a menu/sub-menu option '''

        done = False
        while not done:
            self.screen.blit(self.background_obj.get_image(), (0, 0))  # get background image & blit it on the screen

            '''Check if menu/sub-menu option is clicked. If button is 0 (back/exit button is clicked) break the loop, 
               let menu re-call itself to go back to previous menu '''
            button = self.is_button_clicked()
            if button == 0:
                break

            button_name = button[0]     # button text (str)
            button_font_size = button[2]    # button text size (int)
            num_of_button = len(button[0])  # number of buttons (int)
            drawn_button = [0] * num_of_button  # a list to contain drawn buttons
            rect_pos = button[1]        # rectangle position to blit the button text over
            click = is_mouse_clicked()  # status of the mouse (bool)
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
                    render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i], RED)

                    ''' If button is clicked, make sound effect & push index into the stack (index used to determine 
                        which button is clicked '''
                    if click:
                        audio.play_sound('click')
                        self.stack_obj.push(i)

                        ''' Fade out the screen for nicer visual effects '''
                        self.fade_display()
                        break

            pygame.display.update()

    def fade_display(self):
        """ fade_display -- Fades out the screen when a button is clicked.
        *
        *   INPUT: none
        *
        *   OUTPUT: none
        """
        
        ''' Create a temporarily window for fadeout effects '''
        screen = pygame.display.set_mode((self.width, self.height))
        window = pygame.Surface((screen.get_rect().width, screen.get_rect().height))
        window.fill((0, 0, 0))
        image = self.background_obj.get_image().convert()
        index = 255
        while index >= 0:
            image.set_alpha(index)
            screen.fill((0, 0, 0))
            screen.blit(window, window.get_rect())
            screen.blit(image, image.get_rect())
            index -= 3
            pygame.display.update()

