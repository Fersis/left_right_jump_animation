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
            elif event.key == pygame.K_DOWN:
                guy.down = True
            elif event.key == pygame.K_SPACE:
                guy.jump = True
        # Check key up event
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                guy.moving_left = False
            elif event.key == pygame.K_RIGHT:
                guy.moving_right = False
            elif event.key == pygame.K_DOWN:
                guy.down = False


def update_guy(guy):
    guy.update()


def update_screen(screen, bg, guy):
    """
    Update background and guy 
    """
    screen.blit(bg, screen.get_rect())

    guy.blitme()    
    pygame.display.update()
