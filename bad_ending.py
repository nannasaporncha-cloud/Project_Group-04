import pygame


pygame.init()
WIDTH , HEIGHT = 1500,850
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("You failed")

clock = pygame.time.Clock()
fps = 60

ending_bg = pygame.image.load("assets/bad_scene.png")

def bad_ending():
    running = True

    font = pygame.font.Font(None, 60)
    text = font.render("You lost",True,(255,255,255))
    text_rect = text.get_rect(center=(screen.get_width()//2,screen.get_height()//2 -50))

    sub_font = pygame.font.Font(None,36)
    sub_text = sub_font.render("", True,(220,220,220))
    sub_rect = sub_text.get_rect(center=(screen.get_width()//2,screen.get_height()//2 +40))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
               running = False
               return "quit"
            
        screen.blit(ending_bg,(0,0))

        screen.blit(text, text_rect)
        screen.blit(sub_text,sub_rect)

        pygame.display.update()
        clock.tick(fps)