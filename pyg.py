import pygame, sys
import pygame.locals
BLACK = (0,0,0)
WIDTH = 1280
HEIGHT = 1024
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)
pygame.init()
while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        print("hey")
