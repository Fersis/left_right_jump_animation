from guy import Guy
import sys
import pygame
import glob
from pygame import image
import pygame.display
import pygame.image
import pygame.draw
import pygame.event
from settings import Settings
from guy import Guy


pygame.init()
screen = pygame.display.set_mode((500, 500))


bg = pygame.image.load('images/bg.jpg').convert_alpha()



X = 50
Y = 425
CHA_WIDTH, CHA_HEIGTH = 64, 64
VEL = 5
IS_JUMP = False
JUMP_COUNT = 10
LEFT = False
RIGHT = False
WALKCOUNT = 0

def redraw_game_window():
    """
    Redraw the game window with 
    """
    global WALKCOUNT
    screen.blit(bg, (0, 0))
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (X, Y, CHA_WIDTH, CHA_HEIGTH))
    pygame.display.update()

settings = Settings()

guy = Guy(settings)
# Main loop
while True:
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check key down event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                guy.moving_left == True
            elif event.key == pygame.K_RIGHT:
                guy.moving_right == True
        # Check key up event
        elif event.type == pygame.K_UP:
            if event.key == pygame.K_LEFT:
                guy.moving_left == False
            elif event.key == pygame.K_RIGHT:
                guy.moving_right == False
    
    guy.update()
    redraw_game_window()

