import pygame , sys
from sys import*

#screen
pygame.init()
screenW = 1200
screenH = 800 
tilesize = 50
screen = pygame.display.set_mode((screenW,screenH))

#สี
white = (255,255,255)

def tilemap(self):
    for i, row in enumerate(tilemap):
        for j,column in enumerate(row):
            if column == 'B':
                block(self,j,i)
            elif column == 'a':
                block

                

def update(self):
    self.all_sprites = pygame.sprite.LayeredUpdates()
    self.playing = True

#layer
p_layer = 2
b_layer = 1

tilemap = [
    'aBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBa',
    'a..........................................................a',  
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a..........................................................a',
    'a............................P.............................a',   
    'aBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBa',
]    
class block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = b_layer
        self.group = self.game.all_sprites, self.game.block
        pygame.sprite.Sprite.__init__(self,self.group)
        
        self.x = x*tilesize
        self.y = y*tilesize
        self.screenW = screenW
        self.screenH = screenH
        
        self.image = pygame.Surface([self.screenW,self.screenH])
        self.image.fill(white)
                
        #สร้าง4เหลี่ยม
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
        