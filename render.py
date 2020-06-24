import pygame
BRIGHT_DARK = (20, 20, 20)


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
    pygame.font.init()
    font = pygame.font.Font('munro.ttf', font_size)  # load a custom font from .py dir
    rect = pygame.draw.rect(screen, BRIGHT_DARK, rect_pos)  # draw_render_blit a rectangle.
    render_text = font.render(text, 0, font_color)  # render the text.
    ''' Note: text has to be blited over a geometric shape to be rendered. '''
    screen.blit(render_text, rect)  # render the text over a rectangle

    return rect
