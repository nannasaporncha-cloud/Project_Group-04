import pygame
from setmap import *

class tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,tile_type):
        super().__init__(groups)
        self.image = pygame.Surface((30,30))
        if tile_type == "background":
            self.image.fill((0,0,0))
        elif tile_type == "floor":
            img = pygame.image.load("image/background/floor02.jpg").convert()
            self.image = pygame.transform.scale(img, (tilesize, tilesize))
        elif tile_type == "wall1":
            img = pygame.image.load("image/background/f3.jpg").convert()
            self.image = pygame.transform.scale(img, (tilesize, tilesize))
        elif tile_type == "wall2":
            img = pygame.image.load("image/background/f3.jpg").convert()
            self.image = pygame.transform.scale(img, (tilesize, tilesize))
        self.rect = self.image.get_rect(center=pos)