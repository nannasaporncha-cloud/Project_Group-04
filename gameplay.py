import pygame
from PIL import Image
from player import *
from setting import *
from camera import *

pygame.init()
#ชื่อเกมบนtapbar
pygame.display.set_caption("Exorcist")

#HP
img = Image.open("game/image/assets/hp.png")
hp = 3
heart_images = [pygame.image.load(f"copy_hp_{i}.png") for i in range(1,4)]
heart_size= (50,40)
heart_images = [pygame.transform.scale(img, heart_size) for img in heart_images]

heart_rects = [heart_images[i].get_rect(topleft=(100 + i * (heart_size[0]+10), 20)) for i in range(hp)]  

#score
score = 0
font = pygame.font.Font(None,40)
score_text = font.render(f"Score: {score}", True, WHITE)
score_rect = score_text.get_rect(topleft=(350,30))
HP_text = font.render("HP:", True, WHITE)
HP_rect = score_text.get_rect(topleft=(30,30))


def run_main_game(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #ถ้าผ่านด่านได้รับของscore+1 #ป้อปอัพข้อความได้รับของ
        # ถ้าชนมอน หัวใจลด 
        
        moving_sprites.update()

        screen.fill(WHITE)
        screen.blit(BG,(BG_rect.x - camera_x, BG_rect.y - camera_y))
        screen.blit(score_text, score_rect)
        screen.blit(HP_text, HP_rect)
        for i in range(hp):
            screen.blit(heart_images[i], heart_rects[i])
        camera_group.update()
        camera_group.draw(screen)

        moving_sprites.draw(screen)

        pygame.display.update()
        clock.tick(fps)

    return False  # เปลี่ยนเป็น False หากต้องการออกจากเกมหลัก 