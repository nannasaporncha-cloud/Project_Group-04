import pygame
from setmap import *

class tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,tile_type):
        super().__init__(groups)
        self.image = pygame.Surface((30,30))
        if tile_type == "background":
            self.image.fill((0,0,0))
        elif tile_type == "floor":
            self.image = pygame.image.load("map/img_map/floor2.jpg").convert()
        elif tile_type == "wall1":
            self.image = pygame.image.load("").convert()
        self.rect = self.image.get_rect(topleft=pos)