import pygame


pygame.init()
WIDTH , HEIGHT = 1500,850
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("You failed")

clock = pygame.time.Clock()
fps = 60

bad_end = pygame.image.load("assets/bad_scene.png").convert()
bad_end = pygame.transform.scale(bad_end,(WIDTH,HEIGHT))


def bad_ending():
    running = True

    font = pygame.font.Font(None, 100)
    text = font.render("You lost",True,(255,0,0))
    text_rect = text.get_rect(center=(WIDTH()//2,HEIGHT()//2 -50))

    sub_font = pygame.font.Font(None,36)
    sub_text = sub_font.render("Press Enter to play again", True,(220,220,220))
    sub_rect = sub_text.get_rect(center=(WIDTH()//2,HEIGHT()//2 +40))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
               running = False
               return "quit"
            
        screen.blit(bad_end,(0,0))

        screen.blit(text, text_rect)
        screen.blit(sub_text,sub_rect)

        pygame.display.update()
        clock.tick(fps)