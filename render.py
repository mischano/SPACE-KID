import background
import pygame

BRIGHT_DARK = (18, 6, 38)
index = 0


def draw(screen, text, rect_pos, font_size, font_color):
    (a, b, c, d) = rect_pos
    pygame.font.init()
    font = pygame.font.Font('font/Beon.otf', font_size)  # load a custom font from .py dir
    render_text = font.render(text, 0, font_color)  # render the text.
    s = pygame.Surface((c, d), pygame.SRCALPHA)
    s.fill((0, 0, 0, 0))
    j = screen.blit(s, (a, b))
    screen.blit(render_text, j)  # render the text over a rectangle
    return j


def draw_fade(method1, image, full_screen):
    """
    Fades out the screen when a button is clicked.
    :param method1:
    :param image:
    :param full_screen:
    :return:
    """

    ''' Create a temporarily window for fadeout effects '''
    screen = method1

    window = pygame.Surface((screen.get_rect().width, screen.get_rect().height))
    window.fill((0, 0, 0))
    image = image.convert()
    index = 255
    while index >= 0:
        image.set_alpha(index)
        screen.fill((0, 0, 0))
        screen.blit(window, window.get_rect())
        screen.blit(image, image.get_rect())
        if full_screen is True:
            index -= 1
        else:
            index -= 3
        pygame.display.update()
