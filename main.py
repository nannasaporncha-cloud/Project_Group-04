import pygame
import sys
from setting import*
from background import*

pygame.init()

#ชื่อเกมบนtapbar
pygame.display.set_caption("The Exorcist of Siam")

#charactersize
tilesize = 50

#background
BGf0= pygame.image.load('game/image/BGf0.png').convert_alpha()
BGf0= pygame.transform.scale(BGf0, (tilesize*10, tilesize*8))
BGf0 = BGf0.get_rect()

#player
player = pygame.image.load('game/image/mc_front.png').convert_alpha()
player = pygame.transform.scale(player, (tilesize*2, tilesize*2))

#ตั้งค่าplayer
player_rect = player.get_rect()
player_rect.centerx = screenW //2
player_rect.centery = screenH //2


running =True

#moving
def updeate():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left>0:
        player_rect.x -= speed
    elif keys[pygame.K_RIGHT] and player_rect.right<screenW:
        player_rect.x += speed
    elif keys[pygame.K_UP] and player_rect.top>0:
        player_rect.y -=speed
    elif keys[pygame.K_DOWN] and player_rect.bottom<screenH:
        player_rect.y += speed

def draw():
    screen.fill(white)
    screen_rect = screen.get_rect()
    screen.blit( player,player_rect)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    updeate()
    draw()
    clock.tick(fps)
    
    pygame.display.update()

