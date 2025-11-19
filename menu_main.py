import pygame
import sys
from story_scene import run_story #ไปฉากเกม


pygame.init()
WIDTH , HEIGHT = 1500,850
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game - Menu")

#โหลดรูป เสียง
menu_bg = pygame.image.load("assets/menu_bg.png")
menu_bg = pygame.transform.scale(menu_bg,(WIDTH,HEIGHT))
click_sound = pygame.mixer.Sound("assets/click.mp3")

#เล่นเพลงตั้งเเต่เริ้ม
pygame.mixer.music.load("assets/Thai_intro.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, start= 9.0)

#สี ฟอนต์
RED = (179,0,0)
DARK_GRAY = (20,20,20)
WHITE = (255,255,255)
BLACK = (0,0,0)
title_font = pygame.font.Font(None,96)
button_font = pygame.font.Font(None,48)



start_text = button_font.render("Start",True,WHITE)


#ปุ่ม
button_w, button_h = 260,100
button_x = (WIDTH - button_w) //2
button_y = int(HEIGHT*0.65)
button_rect = pygame.Rect(button_x,button_y,button_w,button_h)

def main():
    running = True
    while running:
        screen.blit(menu_bg,(0,0))
        #shadow ข้อความ
        screen.blit(
            start_text,
            (
                button_x + button_w //2 - start_text.get_width()//2,
                button_y + button_h //2 - start_text.get_height()//2
            )
        )

#ปุ่ม
        pygame.draw.rect(screen,DARK_GRAY,button_rect,border_radius=8)
        # pygame.draw.rect(screen,RED,button_rect,2,border_radius=8)
        text_x = button_x + (button_w // 2) - (start_text.get_width() // 2)
        text_y = button_y + (button_h // 2) - (start_text.get_height() // 2)
        screen.blit(start_text, (text_x, text_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                click_sound.play()
                #ไปหน้าเกม
                run_story(screen)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()