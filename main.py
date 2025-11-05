import pygame
from player import *
from setting import *

pygame.init()

#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    screen.blit(BGf0, BGf0_rect)
    moving_sprites.update()
    moving_sprites.draw(screen)

    pygame.display.update()
    clock.tick(fps)

pygame.quit() 
