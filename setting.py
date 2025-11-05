import pygame
from pathlib import Path


#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")

#sizescreen
screenW = 1540
screenH = 890
center_y = screenW // 2
center_x = screenH // 2
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
BGf0= pygame.image.load('game/image/background/fronthouse.jpg').convert_alpha()
BGf0= pygame.transform.scale(BGf0, (screenW, screenH))
BGf0_rect = BGf0.get_rect(center=(screenW//2, screenH//2))

