import pygame
from pygame.sprite import Sprite

class Guy(Sprite):
    """
    Guy can move right and left and stand
    """
    def __init__(self):
        super().__init__()

        # Movement mark
        self.moving_right = False
        self.moving_left = False

    def update_location(self):
        """
        Move the guy
        """
        if (self.moving_right == True) and ()
