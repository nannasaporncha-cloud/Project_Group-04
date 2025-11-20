import pygame, random, os
from setmap import screenW, screenH, tilesize, inside
from tile import tile

# โหลดภาพผี
ghost_frames = {
    "right": [
        pygame.image.load(os.path.join("image/enemy/ghost1.png")).convert_alpha(),
        pygame.image.load(os.path.join("image/enemy/ghost2.png")).convert_alpha()
    ],
    "left": [
        pygame.image.load(os.path.join("image/enemy/ghost3.png")).convert_alpha(),
        pygame.image.load(os.path.join("image/enemy/ghost4.png")).convert_alpha()
    ]
}

for d in ghost_frames:
    ghost_frames[d] = [pygame.transform.scale(img, (100, 100)) for img in ghost_frames[d]]


class Enemy:
    def __init__(self, all_obstacles):
        # สุ่มตำแหน่งผีบนพื้นที่ "_"
        while True:
            cx = random.randint(1, len(inside[0]) - 2)
            cy = random.randint(1, len(inside) - 2)
            if inside[cy][cx] == "_":
                x = cx * tilesize
                y = cy * tilesize
                break

        self.rect = pygame.Rect(x, y, 70, 100)
        self.speed = random.randint(2, 4)
        self.frame_index = 0
        self.frame_timer = 0
        self.direction = "right"
        self.alpha = 180
        self.target = [x, y]
        self.all_obstacles = all_obstacles

        # HP แบบสุ่ม
        self.max_hp = random.randint(3, 5)
        self.hp = self.max_hp

    # เดินสุ่ม
    def move_random(self):
        if abs(self.rect.x - self.target[0]) < 10 and abs(self.rect.y - self.target[1]) < 10:
            self.target = [
                random.randint(0, screenW),
                random.randint(0, screenH)
            ]

        dx = self.target[0] - self.rect.x
        dy = self.target[1] - self.rect.y

        self.rect.x += self.speed if dx > 0 else -self.speed if dx < 0 else 0
        self.rect.y += self.speed if dy > 0 else -self.speed if dy < 0 else 0

        self.direction = "right" if dx > 0 else "left"

    # ไล่ผู้เล่น
    def chase_player(self, player):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        self.rect.x += self.speed if dx > 0 else -self.speed
        self.rect.y += self.speed if dy > 0 else -self.speed

        self.direction = "right" if dx > 0 else "left"

    # ตรวจชนกำแพง
    def collide_with_walls(self):
        for wall in self.all_obstacles:
            if self.rect.colliderect(wall.rect):
                if self.rect.centerx < wall.rect.centerx:
                    self.rect.right = wall.rect.left
                else:
                    self.rect.left = wall.rect.right

                if self.rect.centery < wall.rect.centery:
                    self.rect.bottom = wall.rect.top
                else:
                    self.rect.top = wall.rect.bottom

    # ตรวจโจมตีโดยตรงใน enemy.py
    def check_attack(self, player):
        # ตรวจว่าผู้เล่นกำลังโจมตี
        if getattr(player, "attacking", False):
            # ขยาย rect ของ player เป็นพื้นที่โจมตี
            attack_rect = player.rect.inflate(20, 20)
            if self.rect.colliderect(attack_rect):
                self.hp -= 1
                print(f"Ghost hit! HP: {self.hp}")
                self.alpha = 255  # ผีสว่างขึ้นเวลาถูกตี

    # อัปเดตผี
    def update(self, player):
        # ไล่ผู้เล่นถ้าใกล้
        dist = abs(player.rect.centerx - self.rect.centerx) + abs(player.rect.centery - self.rect.centery)
        if dist < 350:
            self.chase_player(player)
        else:
            self.move_random()

        self.collide_with_walls()
        self.check_attack(player)  # ตรวจโจมตีโดยตรง

    # วาดผี
    def draw_at(self, surface, pos):
        img = ghost_frames[self.direction][self.frame_index].copy()
        img.set_alpha(self.alpha)
        surface.blit(img, pos)

        # วาด HP bar ตาม pos ด้วย
        hp_ratio = self.hp / self.max_hp
        hp_bar_width = self.rect.width * hp_ratio
        hp_bar = pygame.Rect(pos.x, pos.y - 10, hp_bar_width, 5)
        pygame.draw.rect(surface, (255, 0, 0), hp_bar)


# ตัวช่วยจัดการผีทั้งหมด
class EnemyManager:
    def __init__(self, all_obstacles):
        self.ghosts = []
        self.all_obstacles = all_obstacles

    def spawn_ghost(self, count=5):
        for _ in range(count):
            self.ghosts.append(Enemy(self.all_obstacles))

    def update(self, player):
        # อัปเดตผี และลบผีที่ตาย
        for ghost in self.ghosts[:]:
            ghost.update(player)
            if ghost.hp <= 0:
                self.ghosts.remove(ghost)

    def draw(self, surface,camera_group=None):
        for ghost in self.ghosts:
            if camera_group:
                offset_pos = pygame.math.Vector2(ghost.rect.topleft) - camera_group.offset
                ghost.draw_at(surface, offset_pos)
            else:
                ghost.draw(surface)
