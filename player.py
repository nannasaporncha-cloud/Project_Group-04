import pygame
from pathlib import Path
import setting as s

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group,):
        super().__init__(group)
        # กำหนดขนาดมาตรฐาน
        self.frame_size = (160, 160)
        self.attack_size = (185,185)

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

        #state
        self.current_sprite = 0
        self.current_direction = 'down'
        self.anim_speed = 0.2
        self.image = self.animations['down'][0]
        self.rect = self.image.get_rect(center=pos)

        #sys attack
        self.attacking = False
        self.attack_timer = 0
        self.attack_duration = 150      # เวลาที่ภาพโจมตีค้าง (มิลลิวินาที)
        self.attack_cooldown = 200      # เวลาก่อนจะตีครั้งใหม่ได้
        self.can_attack = True          # ป้องกันกดค้าง
        self.last_dir = 'down'

    def update(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False
        new_dir = None

        # moving
        if keys[pygame.K_a] :
            self.rect.x -= s.speed
            new_dir = 'left'; self.is_moving = True
        elif keys[pygame.K_d] :
            self.rect.x += s.speed
            new_dir = 'right'; self.is_moving = True
        elif keys[pygame.K_w] :
            self.rect.y -= s.speed
            new_dir = 'up'; self.is_moving = True
        elif keys[pygame.K_s] :
            self.rect.y += s.speed
            new_dir = 'down'; self.is_moving = True

        if self.is_moving:
            self.last_dir = new_dir # เก็บท่าล่าสุดที่เดิน
        
        
        if keys[pygame.K_SPACE] and self.can_attack and not self.attacking :
            self.attacking = True
            self.can_attack = False   # ป้องกันกดค้าง
            self.attack_timer = pygame.time.get_ticks()
            # ตั้งทิศทางโจมตีตอนกด SPACE
            if self.last_dir == 'left':
                self.current_direction = 'attackL'
            else:
                self.current_direction = 'attackR'
            
         # รีเซ็ต can_attack เมื่อปล่อยปุ่ม space
        if not keys[pygame.K_SPACE]:
            self.can_attack = True

        # จบการโจมตี → กลับท่าเดิม
        if self.attacking:
            now = pygame.time.get_ticks()
            if now - self.attack_timer >= self.attack_duration:
                self.attacking = False
                self.current_direction = self.last_dir if self.last_dir else 'down'
            
        # เปลี่ยน direction ปกติเมื่อเดิน (ไม่โจมตี)
        if not self.attacking and new_dir:
            if new_dir != self.current_direction:
                self.current_direction = new_dir
                self.current_sprite = 0

        frames = self.animations.get(self.current_direction, self.animations['down'])

        # animation
        if self.is_moving and not self.attacking:
            self.current_sprite += self.anim_speed
            if self.current_sprite >= len(frames):
                self.current_sprite = 0
        else:
            self.current_sprite = 0

        old_center = self.rect.center
        self.image = frames[int(self.current_sprite)]
        self.rect = self.image.get_rect(center=old_center)

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
        ground = pygame.image.load("image/background/floor.png").convert_alpha()
        self.ground_surf = pygame.transform.scale(ground,(1600,1200))
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))
          
    def center_target_camera(self,target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def box_target_camera(self,target):
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        elif target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right

        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        elif target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
        
    def custom_draw(self,player):
        self.box_target_camera(player)

        #ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf,ground_offset)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
            
#camera setup
camera_group = CameraGroup()
player = Player((640,350),camera_group)
