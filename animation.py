import sys
import pygame
from pygame import image
import glob
import pygame.display
import pygame.image
import pygame.draw
import pygame.event


pygame.init()
screen = pygame.display.set_mode((500, 500))

# Read the images
walk_right = [
    pygame.image.load(img).convert_alpha() for img in glob.glob('images/R*.png')
]
walk_left = [
    pygame.image.load(img).convert_alpha() for img in glob.glob('images/L*.png')
]
bg = pygame.image.load('images/bg.jpg').convert_alpha()
char = pygame.image.load('images/standing.png').convert_alpha()


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

# Main loop
while True:
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                


