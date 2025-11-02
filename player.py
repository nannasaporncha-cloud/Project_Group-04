import pygame
from pathlib import Path
from setting import screenW, screenH, white, fps ,speed


# Class Player
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, scale):
        super().__init__()
        self.scale = scale  # อัตราการขยายตัวละคร

        # เก็บแยกรูปตามทิศทาง
        self.animations = {
            'down': [],   # เดินหน้า (ลง)
            'up': [],     # ถอยหลัง (ขึ้น)
            'left': [],   # ซ้าย
            'right': [],  # ขวา
            'attack': [],  # โจมตี
        }

        # กำหนดโฟลเดอร์ฐานสำหรับรูปภาพ 
        base = Path(__file__).parent / 'image' / 'player'
        for name, sub in [('down', 'mc_front'), ('up', 'mc_back'), ('left', 'mc_left'), ('right', 'mc_right')]:
            folder = base / sub
            for i in range(3):
                img_path = folder / f'{i}.png'
                img = pygame.image.load(str(img_path)).convert_alpha()
                w, h = img.get_size()
                img = pygame.transform.scale(img, (int(w * self.scale), int(h * self.scale)))
                self.animations[name].append(img)

        


        self.current_sprite = 0
        self.current_direction = 'down'
        self.anim_speed = 0.17
        self.image = self.animations[self.current_direction][0]
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

        self.is_moving = False
        

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False
        new_dir = None

        # moving
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= speed
            new_dir = 'left'
            self.is_moving = True
        elif keys[pygame.K_d] and self.rect.right < screenW:
            self.rect.x += speed
            new_dir = 'right'
            self.is_moving = True
        elif keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= speed
            new_dir = 'up'
            self.is_moving = True
        elif keys[pygame.K_s] and self.rect.bottom < screenH:
            self.rect.y += speed
            new_dir = 'down'
            self.is_moving = True
        
        
        if keys[pygame.K_SPACE] :
            new_dir = 'attack'
            self.is_moving = True

        
        # เปลี่ยนทิศถ้าแตกต่าง และรีเซ็ตเฟรมเริ่มต้น
        if new_dir and new_dir != self.current_direction:
            self.current_direction = new_dir
            self.current_sprite = 0.0

        frames = self.animations[self.current_direction]

        # animation
        if self.is_moving:
            self.current_sprite += self.anim_speed
            if self.current_sprite >= len(frames):
                self.current_sprite = 0.0
        else:
           self.current_sprite = 0.0

        old_topleft = self.rect.topleft
        self.image = frames[int(self.current_sprite)]
        self.rect = self.image.get_rect(topleft=old_topleft)



# Player setup
player = Player(200, 100, scale=0.6)  
moving_sprites = pygame.sprite.Group()
moving_sprites.add(player)

pygame.init()
pygame.display.set_caption("Exorcist")
screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()

# load background โดยใช้ Path อ้างอิงโฟลเดอร์นี้
base = Path(__file__).parent / 'image' / 'background'
BGf0_path = base / 'BGf0.png'
BGf0 = pygame.image.load(str(BGf0_path)).convert_alpha()
BGf0 = pygame.transform.scale(BGf0, (screenW, screenH))
BGf0_rect = BGf0.get_rect(center=(screenW//2, screenH//2))

player = Player(200, 100, scale=0.6)
moving_sprites = pygame.sprite.Group(player)

