import sys
import pygame.display

def check_event(guy):
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Check key down event
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                guy.moving_left = True
            elif event.key == pygame.K_RIGHT:
                guy.moving_right = True
        # Check key up event
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                guy.moving_left = False
            elif event.key == pygame.K_RIGHT:
                guy.moving_right = False


def update_guy(guy):
    guy.update()


def update_screen(screen, bg, guy):
    """
    Redraw the game window with 
    """

    screen.blit(bg, (0, 0))

    #pygame.draw.rect(screen, (255, 0, 0), (X, Y, CHA_WIDTH, CHA_HEIGTH))
    guy.blitme()    
    pygame.display.update()
