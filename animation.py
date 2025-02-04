import pygame
import pygame.display
import pygame.image
import pygame.draw
import pygame.event
from settings import Settings
from guy import Guy
from pygame.time import Clock
from game_functions import check_event, update_guy, update_screen


pygame.init()

clock = Clock()
screen = pygame.display.set_mode((852, 480))
bg = pygame.image.load('images/bg.jpg').convert_alpha()
settings = Settings()
guy = Guy(settings, screen)

IS_JUMP = False
JUMP_COUNT = 10

# Main loop
while True:
    clock.tick(20)
    
    check_event(guy)

    update_guy(guy)
    
    update_screen(screen, bg, guy)

