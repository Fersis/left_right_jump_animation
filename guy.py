import pygame
import glob
from pygame.sprite import Sprite

class Guy(Sprite):
    """
    Guy can move right and left and stand
    """
    def __init__(self, settings, screen):
        super().__init__()

        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Load walking and standing images
        self.walk_right = [pygame.image.load(img).convert_alpha() 
            for img in glob.glob('images/R*.png')]
        self.walk_left = [pygame.image.load(img).convert_alpha() 
            for img in glob.glob('images/L*.png')]
        self.face_down = pygame.image.load(
            'images/standing.png').convert_alpha()

        # Place character in the middle bottom of screen
        self.rect = self.face_down.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement mark
        self.moving_right = False
        self.moving_left = False

        self.walk_count = 0

        self.pre_walking_right = True

    def update(self):
        """
        Move the guy
        """

        if ((self.moving_right == True) 
                and (self.moving_left == False) 
                and (self.rect.right < self.screen_rect.right)):
            self.rect.centerx += self.settings.walk_speed
            
            self.walk_count += 1
            if self.walk_count > 8:
                self.walk_count = 0
            self.pre_walking_right = True
        
        elif ((self.moving_left == True) 
                and (self.moving_right == False) 
                and (self.rect.left >= self.screen_rect.left)):
            self.rect.centerx -= self.settings.walk_speed
            self.walk_count += 1
            if self.walk_count > 8:
                self.walk_count = 0

            self.pre_walking_right = False

        else:
            self.walk_count = 8

    def blitme(self):
        if ((self.moving_right == True)
                and (self.moving_left == False)):
            self.screen.blit(self.walk_right[self.walk_count], self.rect)
        elif ((self.moving_left == True)
              and (self.moving_right == False)):
            self.screen.blit(self.walk_left[self.walk_count], self.rect)

        else:
            if self.pre_walking_right == True:
                self.screen.blit(self.walk_right[8], self.rect)
            else:
                self.screen.blit(self.walk_left[8], self.rect)

