import pygame
#ไม่ต้องเอาไป merge แค่ตัวอย่างเล่นเกมส์

WIDTH , HEIGHT = 1500, 850

def run_game(screen):
    pygame.display.set_caption("My Game - Playing")

    #โหลดฉากเกม
    game_bg = pygame.image.load("assets/game_bg.png")
    game_bg = pygame.transform.scale(game_bg, (WIDTH,HEIGHT))

    #เพลงพื้นหลัง loop นะจ๊ะ
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("assets/Thai_intro.mp3")
        pygame.mixer.music.play(-1, start= 9.0) #-1 = loop
        pygame.mixer.music.set_volume(0.2)
    except Exception as e:
        print("BGM error:", e)
    
    font = pygame.font.Font(None,30)
    hint = font.render("Press ESC to return to Home", True, (255,255,255))

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #ออกเกม
                pygame.mixer.music.stop()
                pygame.quit()
                # raise SystemExit
                return #ออกจากเกมเลย
            
            #กดESCเพื่อกลับเมนู
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #กลับเมนู
                pygame.mixer.music.fadeout(500) #เสียงจะค่อยๆเบาลงเเล้วหยุด
                playing = False

        #วาดฉากเกม
        screen.blit(game_bg,(0,0))
        screen.blit(hint,(WIDTH//2 - hint.get_width()//2,HEIGHT-60))
        pygame.display.flip()
    return