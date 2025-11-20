import pygame,sys 
from setmap import *
from sprite1 import *
from tile import*

class map:
    def __init__(self):
        self.map_group = pygame.sprite.Group()  # กลุ่ม sprite ของแผนที่ทั้งหมด
        # --- โหลด sprite map --- 
        self.sprite = sprite(self.map_group)
        self.ob_sprites = self.sprite.ob_sprites

    def get_map_group(self):
        return self.map_group
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.sprite.run()
            pygame.display.update()
            self.clock.tick(fps)
            
if __name__ == '__main__':
    game = map() 
    game.run()