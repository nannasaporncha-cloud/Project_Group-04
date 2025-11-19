import pygame, sys
from pygame.locals import *
#from player2 import*

pygame.init()

# ขนาดหน้าจอ
screenW = 1500
screenH = 850
tilesize = 30
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("Tilemap with Background")

# สี
white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 0, 0)

# โหลดรูปฉาก
# ใส่ชื่อไฟล์ภาพของคุณแทน "background.png"
bg = pygame.image.load("img/Bg_img/inhome.jpg").convert()
bg = pygame.transform.scale(bg, (2500, 1850))

#รูปขอบแมพ
con = pygame.image.load("img/Bg_img/conlision.png").convert()
con = pygame.transform.scale(con, (screenW, screenH))

# tilemap
tilemap = [
    'aBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBa',
    'a........................................................................................................a',
    'a........................................................................................................a',
    'a........................................................................................................a',
    'a......BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......a.........................................................................................a.......a',
    'a......BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB--BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB.......a',
    'a........................................................................................................a',
    'a........................................................................................................a',
    'a........................................................................................................a',
    'aBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBa',
]

# กลุ่ม Sprite
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# คลาส Block
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__(all_sprites, blocks)
        self.image = pygame.Surface((tilesize, tilesize))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x * tilesize
        self.rect.y = y * tilesize
        all_sprites.draw(screen)
    
    # def conclision():
        

# ฟังก์ชันสร้าง tilemap
def draw_tilemap():
    for y, row in enumerate(tilemap):
        for x, tile in enumerate(row):
            if tile == 'B' or tile == 'a':
                Block(x, y, red)
            elif tile == '-':
                Block(x, y,white)

draw_tilemap()

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # วาดฉากพื้นหลัง
    screen.blit(bg, (0, 0))
    
    pygame.display.flip()

    pygame.display.flip()
    clock.tick(60)