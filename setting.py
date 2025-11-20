import pygame

pygame.init()

#sizescreen
screenW ,screenH = 1500,850
screen = pygame.display.set_mode((screenW,screenH))

#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")
screen_rect = screen.get_rect()

#center
center_x = screenW // 2
center_y = screenH // 2

#ตั้งค่าสีRGB
RED = (179,0,0)
DARK_GRAY = (20,20,20)
WHITE = (255,255,255)
BLACK = (0,0,0)

#movespeed
speed = 3

#FPS
fps = 30
clock = pygame.time.Clock()

ground = pygame.image.load("image/background/floor02.jpg").convert_alpha()
ground_surf = pygame.transform.scale(ground,(1600,1200))
ground_rect = ground_surf.get_rect(topleft=(0,0))