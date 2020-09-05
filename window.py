import background
import properties
import render
import pygame
import status
import audio
import stack


class Display:
    def __init__(self, width, height, fs, fps):
        self.width = width
        self.height = height
        self.full_screen = fs
        self.fps = fps
        self.screen = 0  # menu window object.

        self.stack_obj = stack.Stack()
        self.background_obj = background.Background(self.width, self.height)

    def init_window(self):
        """
        Set up a new window.
        :return: display surface
        """
        pygame.init()
        if not self.full_screen:
            screen = pygame.display.set_mode((self.width, self.height))
        else:
            screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)

        pygame.display.set_caption(properties.GAME_TITLE)  # Title, top left corner.

        return screen

    def display(self):
        """
        Displays the window on the screen.
        :return: to calling function
        """
        button = status.is_button_clicked(self.stack_obj)
        if button == 0:  # Return if back button is clicked.
            return

        button_name = button[0]  # button text (str)
        button_font_size = button[2]  # button text size (int)
        num_of_button = len(button[0])  # number of buttons (int)
        drawn_button = [0] * num_of_button  # a list to contain drawn buttons
        rect_pos = button[1]  # rectangle position to blit the button text over
        # a range of text that can be highlighted & clicked.
        _min = button[3][0]
        _max = button[3][1]

        sound = -1
        collide = -1
        done = False
        while not done:
            self.screen.blit(self.background_obj.get_image(), (0, 0))
            for i in range(num_of_button):
                if collide == i:
                    (a, b, c, d) = rect_pos[i]
                    drawn_button[i] = render.draw(self.screen, button_name[i], (a, b, (c + c * 0.2), d),
                                                  button_font_size[i],
                                                  properties.DARK_WHITE)
                else:
                    drawn_button[i] = render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i],
                                                  properties.DARK_WHITE)

            click = status.is_mouse_clicked()  # status of the mouse (bool)
            # In the range of collidable buttons.
            for i in range(int(_min), int(_max)):
                if drawn_button[i].collidepoint(pygame.mouse.get_pos()):
                    collide = i
                    if sound != i:  # Hover sound effect
                        audio.play_sound('hower')
                        sound = i  # To play sound only once per collision.
                    ''' Re-draw in red color.'''
                    self.screen.blit(self.background_obj.get_image(), (0, 0))
                    for j in range(num_of_button):
                        if j == i:
                            pass
                        else:
                            drawn_button[j] = render.draw(self.screen, button_name[j], rect_pos[j],
                                                          button_font_size[j],
                                                          properties.DARK_WHITE)
                    render.draw(self.screen, button_name[i], rect_pos[i], button_font_size[i] + 10, properties.RED)

                    # If the button is clicked.
                    if click:
                        audio.play_sound('click')
                        pygame.time.delay(200)
                        self.stack_obj.push(i)
                        # Fade out the screen.
                        render.draw_fade(self.init_window(), self.background_obj.get_image(), self.full_screen)

                        return

            pygame.display.update()
