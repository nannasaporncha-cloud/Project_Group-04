import pygame
from setmap import*
from tile import*


class sprite:
    def __init__(self):
        
        #วาดแมป
        pygame.init()
        self.display_surface = pygame.display.get_surface()
        
        # การตั้งค่า กลุ่มsprite
        self.visible_sprites = pygame.sprite.Group()
        self.ob_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.createmap()
    
    #กำหนดตำแหน่ง    
    def createmap(self):
        for row_index,row in enumerate(inside):
            for col_index, col in enumerate(row):
                x = int(col_index * tilesize)
                y = int(row_index * tilesize)
                if col == '.':
                    tile((x,y),[self.visible_sprites], "background")
                elif col == '_':
                    tile((x,y),[self.visible_sprites],"floor")
    def run(self):
        #การรันการวาดแมป
        self.visible_sprites.draw(self.display_surface)         