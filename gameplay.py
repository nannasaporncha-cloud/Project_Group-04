import pygame
from PIL import Image
from player import *
from setting import *

pygame.init()
#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")

#HP
#img = Image.open("game/image/assets/hp.png")
hp = 5
heart_images = pygame.image.load("game/image/assets/hp.png").convert_alpha()
heart_size= (50,40)
heart_images = pygame.transform.scale(heart_images,heart_size) 

#score
score = 0
font = pygame.font.Font(None,40)
score_text = font.render(f"Score: {score}", True, WHITE)
score_rect = score_text.get_rect(topleft=(500,30))
HP_text = font.render("HP:", True, WHITE)
HP_rect = score_text.get_rect(topleft=(50,30))

def run_main_game(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #ถ้าผ่านด่านได้รับของscore+1 #ป้อปอัพข้อความได้รับของ
        # ถ้าชนมอน หัวใจลด 
        
        moving_sprites.update()

        screen.fill(BLACK)
        camera_group.update()
        camera_group.custom_draw(player)
        moving_sprites.draw(screen)

        screen.blit(score_text, score_rect)
        screen.blit(HP_text, HP_rect)
        for i in range(hp):
            x = 100 +i *(heart_size[0]+10)
            screen.blit(heart_images,(x,20) )
        
        pygame.display.update()
        clock.tick(fps)

    return False  # เปลี่ยนเป็น False หากต้องการออกจากเกมหลัก 