import pygame
import glob
from pygame.sprite import Sprite

class Guy(Sprite):
    """
    Control walking
    """
    def __init__(self, settings, screen):
        super().__init__()

        self.settings = settings
        self.screen = screen

        self.screen_rect = self.screen.get_rect()

        # Load walking and face_down images
        self.walk_right = [pygame.image.load(img).convert_alpha() 
            for img in glob.glob('images/R*.png')]
        self.walk_left = [pygame.image.load(img).convert_alpha() 
            for img in glob.glob('images/L*.png')]
        self.face_down = pygame.image.load(
            'images/standing.png').convert_alpha()

        # Place character in the middle bottom of screen
        self.rect = self.face_down.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.bottom -= 10

        # Walking direction of previous status
        self.pre_walking_right = 'down'

        # Movement mark
        self.moving_right = False
        self.moving_left = False
        self.walk_count = 0
        self.down = False
        self.jump = False
        self.jump_time = 1

    def update(self):
        """
        Update walking images and position
        """
        # Jumping
        if self.jump == True:
            self.rect.bottom = self.screen_rect.bottom -10 + int(
                self.settings.v0 * self.jump_time 
                - 0.5 * self.settings.G * self.jump_time ** 2
            )
            self.jump_time += 1
        # Face down
        if self.down == True:
            self.pre_walking_right = 'down'
        # Moving right
        elif ((self.moving_right == True) 
                and (self.moving_left == False) 
                and (self.rect.right < self.screen_rect.right)):
            self.rect.centerx += self.settings.walk_speed           
            self.walk_count += 1
            if self.walk_count > 8:
                self.walk_count = 0
            self.pre_walking_right = 'right'
        # Moving left
        elif ((self.moving_left == True) 
                and (self.moving_right == False) 
                and (self.rect.left >= self.screen_rect.left)):
            self.rect.centerx -= self.settings.walk_speed
            self.walk_count += 1
            if self.walk_count > 8:
                self.walk_count = 0
            self.pre_walking_right = 'left'
        # User doesn't press any directon keys 
        # or press left key and right key simultaneously
        else:
            self.walk_count = 8

    def blitme(self):
        """
        Blit the images corresponding to walking status.
        """
        # Face down
        if self.down == True:
            self.screen.blit(self.face_down, self.rect)
        # Walking right
        elif ((self.moving_right == True)
                and (self.moving_left == False)):
            self.screen.blit(self.walk_right[self.walk_count], self.rect)
        # Walking left
        elif ((self.moving_left == True)
                and (self.moving_right == False)):
            self.screen.blit(self.walk_left[self.walk_count], self.rect)
        # Standing
        else:
            if self.pre_walking_right == 'down':
                self.screen.blit(self.face_down, self.rect)
            elif self.pre_walking_right == 'right':
                self.screen.blit(self.walk_right[8], self.rect)
            elif self.pre_walking_right == 'left':
                self.screen.blit(self.walk_left[8], self.rect)

