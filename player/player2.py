import pygame
from pathlib import Path
import setting as s

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,):
        super().__init__()
        # กำหนดขนาดมาตรฐาน
        self.frame_size = (130, 130)
        self.attack_size = (150,150)

        self.animations = {
            'down': [],  
            'up': [],    
            'left': [],   
            'right': [],  
            'attack': [],  
        }

        # กำหนดโฟลเดอร์ฐานสำหรับรูปภาพ 
        base = Path(__file__).parent /'img'
        for name, sub in [('down', 'mc_front'), ('up', 'mc_back'), ('left', 'mc_left'), ('right', 'mc_right')]:
            folder = base / sub
            for i in range(3):
                img = folder / f'{i}.png'
                img = pygame.image.load(str('img_path')).convert_alpha()
                img = pygame.transform.scale(img, self.frame_size)
                self.animations[name].append(img)

        attackL = pygame.image.load('img\mc_attack\L.png').convert_alpha()
        attackR = pygame.image.load("img\mc_attack\R.png").convert_alpha()
        
        self.attackL = pygame.transform.scale(attackL,self.attack_size)
        self.attackR = pygame.transform.scale(attackR,self.attack_size)
    
        self.animations['attackL'] = [self.attackL,]
        self.animations['attackR'] = [self.attackR,]

        self.attacking = False
        self.attack_timer = 0
        self.attack_duration = 30  

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
            for sprite in self.game.all_sprite: 
                    sprite.rect.x += self.anim_speed
            self.rect.x -= s.speed
            new_dir = 'left'
            self.is_moving = True
        elif keys[pygame.K_d] and self.rect.right < s.screenW:
            for sprite in self.game.all_sprite: 
                    sprite.rect.x += self.anim_speed
            self.rect.x += s.speed
            new_dir = 'right'
            self.is_moving = True
        elif keys[pygame.K_w] and self.rect.top > 0:
            for sprite in self.game.all_sprite: 
                    sprite.rect.x += self.anim_speed
            self.rect.y -= s.speed
            new_dir = 'up'
            self.is_moving = True
        elif keys[pygame.K_s] and self.rect.bottom < s.screenH:
            for sprite in self.game.all_sprite: 
                    sprite.rect.x += self.anim_speed
            self.rect.y += s.speed
            new_dir = 'down'
            self.is_moving = True
        
        
        
        if keys[pygame.K_SPACE] :
            if keys[pygame.K_a]:  
                new_dir = 'attackL'
            elif keys[pygame.K_d] :  
                new_dir = 'attackR'
                
            self.attacking = True
            self.attack_timer = pygame.time.get_ticks()
            self.is_moving = True

        # ตัวจับเวลาการโจมตี
        if self.attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.attacking = False
                new_dir = self.current_direction  # กลับไปทิศทางเดิม

        
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

        old_topleft = self.rect.topleft
        self.image = frames[int(self.current_sprite)]
        self.rect = self.image.get_rect(topleft=old_topleft)

# Player setup
player = Player(s.center_y-25, s.center_x+250,)  
moving_sprites = pygame.sprite.Group()
moving_sprites.add(player)

