import pygame
from settings import *
import sys
pygame.init()

def timer(screen):

    done = False
    secs = 0
    mins = 0

    text = START_FONT.render(f'{mins}:{secs}', True, WHITE, BLACK)
    textRect = text.get_rect()
    textRect.center(WIDTH//2, HEIGHT//2)

    clock = pygame.time.Clock()

    while not done:
        clock.tick(1)
        secs += 1
        screen.blit(text,textRect)
        if secs == 60:
            secs = 0
            mins += 1
        text = START_FONT.render(f'{mins}:{secs}', True, WHITE, BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
