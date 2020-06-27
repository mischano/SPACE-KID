import pygame

BRIGHT_DARK = (18, 6, 38)
index = 0


def draw(screen, text, rect_pos, font_size, font_color):
    """ draw_render_blit: Draws a rectangle, renders a text, & blits over a rectangle.
            args:
                text (str): string text
                text_pos (tuple): rectangle coordinates
                font_size (int): size of the font
                font_color (tuple): RGB color
            return:
                rectangle (tuple) - rectangle coordinates
        """
    (a, b, c, d) = rect_pos
    # print(a, b, c, d)
    pygame.font.init()
    font = pygame.font.Font('font/Beon.otf', font_size)  # load a custom font from .py dir
    # rect = pygame.draw.rect(screen, BRIGHT_DARK, rect_pos)  # draw_render_blit a rectangle.
    render_text = font.render(text, 0, font_color)  # render the text.
    ''' Note: text has to be blited over a geometric shape to be rendered. '''
    # screen.blit(render_text, rect)  # render the text over a rectangle

    s = pygame.Surface((200, 60), pygame.SRCALPHA)
    s.fill((0, 0, 0, 0))
    j = screen.blit(s, (a, b))
    screen.blit(render_text, j)  # render the text over a rectangle
    return j
