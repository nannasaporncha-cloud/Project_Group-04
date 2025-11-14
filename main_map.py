import pygame,sys 
from setmap import *

class map:
    def __init__(self):
        # ตั้งค่าทั่วไป
        pygame.init()
        self.screen = pygame.display.set_mode((screenW,screenH))
        self.clock = pygame.time.Clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(fps)
            
if __name__ == '__main__':
    game = map()
    game.run()