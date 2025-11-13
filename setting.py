import pygame

pygame.init()

#sizescreen
screenW = 1500
screenH = 850
screen = pygame.display.set_mode((screenW,screenH))

#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")
screen_rect = screen.get_rect()

#center
center_y = screenW // 2
center_x = screenH // 2

#ตั้งค่าสีRGB
RED = (179,0,0)
DARK_GRAY = (20,20,20)
WHITE = (255,255,255)
BLACK = (0,0,0)

#movespeed
speed = 5

#FPS
fps = 30
clock = pygame.time.Clock()

#background
BG= pygame.image.load('game/image/background/fronthouse.jpg').convert_alpha()
BG= pygame.transform.scale(BG, (screenW, screenH))
BG_rect = BG.get_rect(center=(screenW//2, screenH//2))

