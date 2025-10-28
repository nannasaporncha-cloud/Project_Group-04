import pygame

pygame.init()

#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")

#charactersize
tilesize = 50

#sizescreen
screenW = 1200
screenH = 800
screen = pygame.display.set_mode((screenW,screenH))
screen_rect = screen.get_rect()

#ตั้งค่าสีRGB
white = (255,255,255)

#movespeed
speed = 5

#FPS
fps = 30
clock = pygame.time.Clock()

#background
BGf0= pygame.image.load('game/image/background/BGf0.png').convert_alpha()
BGf0= pygame.transform.scale(BGf0, (screenW, screenH))
BGf0_rect = BGf0.get_rect()

#player
player = pygame.image.load('game/image/player/mc_front/chisom_front.png').convert_alpha()
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
    screen.blit( BGf0,BGf0_rect)
    screen.blit( player,player_rect)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    print(player_rect)
            
    updeate()
    draw()
    clock.tick(fps)
    
    pygame.display.update()

