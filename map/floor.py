import pygame
from setmap import *

class tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,tile_type):
        super().__init__(groups)
        self.image = pygame.image.load("map/img_map/floor.jpg").convert()
        if tile_type == "floor":
            self.image = pygame.image.load("map/img_map/floor.jpg").convert()
        self.rect = self.image.get_rect(topleft=pos)