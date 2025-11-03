import pygame
import player as p
from pathlib import Path

pygame.init()

#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")

#charactersize
tilesize = 50

#sizescreen
screenW = 1540
screenH = 890
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

def draw():
    screen.fill(white)
    screen.blit( BGf0,BGf0_rect)
    screen.blit( p.player,p.player_rect)

# load background โดยใช้ Path อ้างอิงโฟลเดอร์นี้
base = Path(__file__).parent / 'image' / 'background'
BGf0_path = base / 'BGf0.png'
BGf0 = pygame.image.load(str(BGf0_path)).convert_alpha()
BGf0 = pygame.transform.scale(BGf0, (screenW, screenH))
BGf0_rect = BGf0.get_rect(center=(screenW//2, screenH//2))

