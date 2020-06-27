from pygame.locals import *
import properties
import sys
import pygame


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


def is_button_clicked(stack):
    """ is_button_clicked -- Checks the status of menu buttons. Specifically, if any of the menu buttons are clicked.
    *
    *   INPUT: none
    *
    *   OUTPUT: button -- 2D list - containing text & rectangle properties of a menu/sub-menu to be drawn
    """

    # If variable is not initialized: Local variable 'button' might be referenced before assignment - warning occurs
    button = None

    ''' If the stack size is (0), return main menu button properties '''
    if stack.size() == 0:
        button = properties.get_properties(0)

    else:
        ''' If the top value of the stack is (0), back/exit button is clicked '''
        if stack.peek() == 0:

            ''' If the stack size is 1, Exit button is clicked. Call exit method & exit the menu '''
            if stack.size() == 1:
                exit_game()

            else:
                ''' Else, (back button is clicked) pop the last 2 values (refer to stack class for more information) 
                    & return (0) to be handled in display method '''
                stack.pop()
                return 0
        else:
            ''' If the top value of the stack is not (0), load the sub-menu properties of the clicked button 
                according to stack values & size '''
            button = properties.get_properties(stack.size())[stack.peek()]

    return button

