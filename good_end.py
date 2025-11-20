import pygame

pygame.init()
WIDTH , HEIGHT = 1500,850
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The End")

clock = pygame.time.Clock()
fps = 60

ending_bg = pygame.image.load("image/assets/good_ending.png")

def run_ending():
    running = True

    thai_font = "assets/THsarabaneiei.ttf"
    font = pygame.font.Font(thai_font, 60)
    text = font.render("ฉันทำได้แล้วสินะ...",True,(255,255,255))
    text_rect = text.get_rect(center=(screen.get_width()//2,screen.get_height()//2 -50))

    sub_font = pygame.font.Font(thai_font,36)
    sub_text = sub_font.render("กด Enter เพื่อจบเกม", True,(220,220,220))
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

# import pygame
# pygame.init()
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("TEST ENDING WINDOW")
# clock = pygame.time.Clock()
# fps = 60
# def run_ending():
#    running = True
#    while running:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                running = False
#        screen.fill((0, 0, 0))  # พื้นหลังดำเฉยๆ
#        pygame.display.update()
#        clock.tick(fps)
# run_ending()
# pygame.quit()


