import pygame

pygame.init()
WIDTH , HEIGHT = 1500,850
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("You failed")

clock = pygame.time.Clock()
fps = 60

ending_bg = pygame.image.load("image/assets/bad_scene.png")

def bad_ending():
    running = True

    font = pygame.font.Font(None, 60)
    text = font.render("You lost",True,(255,255,255))
    text_rect = text.get_rect(center=(screen.get_width()//2,screen.get_height()//2 -50))

    sub_font = pygame.font.Font(None,36)
    sub_text = sub_font.render("", True,(220,220,220))
    sub_rect = sub_text.get_rect(center=(screen.get_width()//2,screen.get_height()//2 +40))

    #ปุ่ม retry
    btn_font = pygame.font.Font(None, 48)
    retry_text = btn_font.render("Retry", True, (0,0,0))
    retry_rect = pygame.Rect(0, 0, 220, 70)
    retry_rect.center = (screen.get_width()//2, screen.get_height()//2 + 200)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_rect.collidepoint(event.pos):
                    return "retry"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
               running = False
               return "retry"
            
        screen.blit(ending_bg,(0,0))

        screen.blit(text, text_rect)
        screen.blit(sub_text,sub_rect)

        pygame.draw.rect(screen, (255,255,255), retry_rect, border_radius=12)
        retry_text_rect = retry_text.get_rect(center=retry_rect.center)
        screen.blit(retry_text, retry_text_rect)

        pygame.display.update()
        clock.tick(fps)