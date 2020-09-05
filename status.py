from pygame.locals import *
import properties
import sys
import pygame


def exit_game():
    """ exit_game: Exit pygame & program. """
    pygame.quit()
    sys.exit()


def is_mouse_clicked():
    """
    Checks the status of the mouse.
    :return:   bool - True if moused clicked, False otherwise
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                return True
            else:
                return False


def is_button_clicked(stack):
    """
    Checks if any of the menu buttons are clicked.
    :param stack: stack object
    :return: 2D list - contains properties of a menu/sub-menu to be drawn
    """
    button = None

    # If stack is empty, display the main menu.
    if stack.size() == 0:
        button = properties.get_properties(0)
    else:
        # If the top value of the stack is 0, back/exit button is clicked.
        if stack.peek() == 0:
            # If the stack size is 1, Exit button is clicked.
            if stack.size() == 1:
                exit_game()
            # Else, Back button is clicked.
            else:
                stack.pop()
                return 0
        # Else, load sub-menu properties according to button clicked.
        else:
            button = properties.get_properties(stack.size())[stack.peek()]

    return button
