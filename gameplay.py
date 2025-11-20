import pygame
from player import *
from setting import *
from main_map import map
from enemy import Enemy ,EnemyManager

pygame.init()
#ชื่อเกมบนtapbar
pygame.display.set_caption("The exorcist-Playing")

#HP
hp = 5
heart_images = pygame.image.load("image/assets/hp.png").convert_alpha()
heart_size= (50,40)
heart_images = pygame.transform.scale(heart_images,heart_size) 

#score
score = 0
font = pygame.font.Font(None,40)
score_text = font.render(f"Score: {score}", True, WHITE)
score_rect = score_text.get_rect(topleft=(500,30))
HP_text = font.render("HP:", True, WHITE)
HP_rect = score_text.get_rect(topleft=(50,30))


#โหลดฉากเกม
game_bg = pygame.image.load("image/assets/game_bg.png")
game_bg = pygame.transform.scale(game_bg, (screenW,screenH))

#เพลงพื้นหลัง loop นะจ๊ะ
try:
    pygame.mixer.init()
    pygame.mixer.music.load("image/assets/Thai_intro.mp3")
    pygame.mixer.music.play(-1, start= 9.0) #-1 = loop
    pygame.mixer.music.set_volume(0.2)
except Exception as e:
    print("BGM error:", e)
    
font = pygame.font.Font(None,40)
hint = font.render("Press ESC to return to Home", True, (255,255,255))

#camera setup
camera_group = CameraGroup()
player = Player((640,350),camera_group)

# โหลด map
game_map = map()
map_group = game_map.get_map_group()
obstacles = game_map.ob_sprites

enemy_manager = EnemyManager(obstacles)
enemy_manager.spawn_ghost(5)


def run_main_game(screen):
    global hp, score
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #กลับเมนู
                pygame.mixer.music.fadeout(500) #เสียงจะค่อยๆเบาลงเเล้วหยุด
                running = False
        
        camera_group.update(obstacles=obstacles)
        player.update(obstacles) # <-- Update player กับ obstacles 

        screen.fill(BLACK)
        camera_group.custom_draw(player,map_group)
        
        enemy_manager.update(player)  # ไม่ต้องส่ง attack_rect แล้ว
        enemy_manager.draw(screen,camera_group)


        score_text = font.render(f"Score: {score}", True, WHITE)
        HP_text = font.render("HP:", True, WHITE)
        screen.blit(score_text, score_rect)
        screen.blit(HP_text, HP_rect)

        for i in range(hp):
            x = 100 +i *(heart_size[0]+10)
            screen.blit(heart_images,(x,20) )
        
        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)


    return 