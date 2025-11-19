import pygame
from setmap import*
from tile import*
from player import Player,CameraGroup

#ศึกษาเองจากคลิปhttps://youtu.be/QU1pPzEGrqw?si=1OlyZ8YuXitHg5W4

class sprite:
    def __init__(self):
        
        #วาดแมป
        pygame.init()
        self.display_surface = pygame.display.get_surface()
        
        # การตั้งค่า กลุ่มsprite
        self.visible_sprites = pygame.sprite.Group()
        self.ob_sprites = pygame.sprite.Group()
        
        #กล้องที่มาจากเพลเยอรื
        camera_group = CameraGroup()
        camera_group.sprites_group = self.visible_sprites
        
        # sprite setup
        self.createmap()
        self.player = Player((640, 350), self.visible_sprites)
    
    #กำหนดตำแหน่ง    
    def createmap(self):
        for row_index,row in enumerate(inside):
            for col_index, col in enumerate(row):
                x = int(col_index * tilesize)
                y = int(row_index * tilesize)
                if col == '.':
                    tile((x,y),[self.visible_sprites,self.ob_sprites], "background")
                elif col == '_':
                    tile((x,y),[self.visible_sprites],"floor")
                elif col == 'w':
                    tile((x,y),[self.visible_sprites,self.ob_sprites], "wall1")
                elif col == 'W':
                    tile((x,y),[self.visible_sprites,self.ob_sprites], "wall2")
    def run(self):
        #การรันการวาดแมป
        self.visible_sprites.update(self.ob_sprites)
        self.visible_sprites.draw(self.display_surface)