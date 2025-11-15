import pygame
from pathlib import Path
import setting as s

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,):
        super().__init__()
        # กำหนดขนาดมาตรฐาน
        self.frame_size = (160, 160)
        self.attack_size = (180,180)

        self.animations = {
            'down': [],  
            'up': [],    
            'left': [],   
            'right': [],  
            'attack': [],  
        }

        # กำหนดโฟลเดอร์ฐานสำหรับรูปภาพ 
        base = Path(__file__).parent / 'image' / 'player'
        for name, sub in [('down', 'mc_front'), 
                          ('up', 'mc_back'), 
                          ('left', 'mc_left'), 
                          ('right', 'mc_right')]:
            folder = base / sub
            for i in range(3):
                img_path = folder / f'{i}.png'
                img = pygame.image.load(str(img_path)).convert_alpha()
                img = pygame.transform.scale(img, self.frame_size)
                self.animations[name].append(img)

        attackL = pygame.image.load(str(base / 'mc_attack' / 'L.png')).convert_alpha()
        attackR = pygame.image.load(str(base / 'mc_attack' / 'R.png')).convert_alpha()
        self.animations['attackL'] = [pygame.transform.scale(attackL, self.attack_size)]
        self.animations['attackR'] = [pygame.transform.scale(attackR, self.attack_size)]

        self.is_moving = False
        self.attacking = False
        self.attack_timer = 0
        self.attack_duration = 0  

        self.current_sprite = 0
        self.current_direction = 'down'
        self.anim_speed = 0.2
        self.image = self.animations[self.current_direction][0]
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False
        new_dir = None

        # moving
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= s.speed
            new_dir = 'left'
            self.is_moving = True
        elif keys[pygame.K_d] and self.rect.right < s.screenW:
            self.rect.x += s.speed
            new_dir = 'right'
            self.is_moving = True
        elif keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= s.speed
            new_dir = 'up'
            self.is_moving = True
        elif keys[pygame.K_s] and self.rect.bottom < s.screenH:
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

        # ตัวจับเวลาการโจมตี
        if self.attacking:
            now = pygame.time.get_ticks()
            if now - self.attack_timer > self.attack_duration:  # ถ้าเกินเวลาที่กำหนด
                self.attacking = False
                new_dir = self.current_direction  # กลับไปทิศทางเดิม
            
        # เปลี่ยนทิศถ้าแตกต่าง และรีเซ็ตเฟรมเริ่มต้น
        if new_dir and new_dir != self.current_direction:
            self.current_direction = new_dir
            self.current_sprite = 0

        frames = self.animations[self.current_direction]

        # animation
        if self.is_moving or self.attacking:
            self.current_sprite += self.anim_speed
            if self.current_sprite >= len(frames):
                self.current_sprite = 0.0
        else:
            self.current_sprite = 0.0

        old_topleft = self.rect.topleft
        self.image = frames[int(self.current_sprite)]
        self.rect = self.image.get_rect(topleft=old_topleft)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset 
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] //2
        self.half_h = self.display_surface.get_size()[1] //2
          
        # box setup
        self.camera_borders = {'left': 100, 'right': 100, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)
          
        #ground
        ground = pygame.image.load("game/image/background/floor.png").convert_alpha()
        self.ground_surf = pygame.transform.scale(ground,(1600,1200))
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))
          
    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def box_target_camera(self,target):
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
        
    def custom_draw(self,player):
        self.center_target_camera(player)

        #ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf,ground_offset)

        pygame.draw.rect(self.display_surface,'yellow',self.camera_rect,5)
        
            
#camera setup
camera_group = CameraGroup()

# Player setup
player = Player((750,500),camera_group)
moving_sprites = pygame.sprite.Group()
moving_sprites.add(player)
