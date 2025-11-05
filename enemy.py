import pygame, random, os
from player import player, moving_sprites  # ← ตัวละครหลักจาก player.py
from setting import screen, clock, BGf0, BGf0_rect, white, fps  # ← จอ + พื้นหลัง

pygame.display.set_caption("Exorcist")

# === โหลดภาพผี ===
ghost_frames = {
    "right": [
        pygame.image.load(os.path.join("image/enemy/ghost0.png")).convert_alpha(),
        pygame.image.load(os.path.join("image/enemy/ghost1.png")).convert_alpha()
    ],
    "left": [
        pygame.image.load(os.path.join("image/enemy/ghost2.png")).convert_alpha(),
        pygame.image.load(os.path.join("image/enemy/ghost3.png")).convert_alpha()
    ],
    "up": [
        pygame.image.load(os.path.join("image/enemy/ghost4.png")).convert_alpha(),
        pygame.image.load(os.path.join("image/enemy/ghost5.png")).convert_alpha()
    ],
    "down": [
        pygame.image.load(os.path.join("image/enemy/ghost6.png")).convert_alpha(),
        pygame.image.load(os.path.join("image/enemy/ghost7.png")).convert_alpha()
    ]
}
for d in ghost_frames:
    ghost_frames[d] = [pygame.transform.scale(img, (40,80)) for img in ghost_frames[d]]

# === สร้างผี ===
ghost = pygame.Rect(200, 200, 50, 120)
speed = 2
frame_index = 0
frame_timer = 0
direction = "right"
ghost_state = "active"
ghost_alpha = 150
hit_time = 0
player_can_move = True

# === กำหนดพื้นที่ที่ผีจะเดินสุ่มได้ ===
room = pygame.Rect(100, 100, 1340, 700)
target = [random.randint(room.left, room.right),
          random.randint(room.top, room.bottom)]


# ---------- ฟังก์ชันการเคลื่อนที่ผี ----------
def move_random():
    global target, direction
    if abs(ghost.x - target[0]) < 5 and abs(ghost.y - target[1]) < 5:
        target = [random.randint(room.left, room.right),
                  random.randint(room.top, room.bottom)]

    dx, dy = target[0] - ghost.x, target[1] - ghost.y

    # เคลื่อนที่เข้าเป้าหมาย
    if dx > 0:
        ghost.x += speed
    elif dx < 0:
        ghost.x -= speed

    if dy > 0:
        ghost.y += speed
    elif dy < 0:
        ghost.y -= speed

    # ใช้ภาพตามแนวแกน X เป็นหลัก
    if dx > 0:
        direction = "right"
    elif dx < 0:
        direction = "left"
    # ถ้า dx = 0 ให้คงภาพเดิมไว้


def chase_player():
    global direction
    dx = player.rect.centerx - ghost.centerx
    dy = player.rect.centery - ghost.centery

    # ขยับเข้าใกล้ผู้เล่น
    if dx > 0:
        ghost.x += speed
    elif dx < 0:
        ghost.x -= speed

    if dy > 0:
        ghost.y += speed
    elif dy < 0:
        ghost.y -= speed

    # ใช้ภาพตามแนวแกน X เป็นหลัก
    if dx > 0:
        direction = "right"
    elif dx < 0:
        direction = "left"

def keep_inside_room():
    if ghost.left < room.left: ghost.left = room.left
    if ghost.right > room.right: ghost.right = room.right
    if ghost.top < room.top: ghost.top = room.top
    if ghost.bottom > room.bottom: ghost.bottom = room.bottom


# ---------- ลูปหลัก ----------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # ให้ player ขยับได้เฉพาะตอนที่ไม่โดนผี
    if player_can_move:
        player.update()

    # === อัปเดตผี ===
    if ghost_state == "active":
        if room.collidepoint(player.rect.center):
            chase_player()
        else:
            move_random()
        keep_inside_room()

        frame_timer += 1
        if frame_timer >= 15:
            frame_timer = 0
            frame_index = (frame_index + 1) % len(ghost_frames[direction])

        if ghost.colliderect(player.rect):
            ghost_state = "hit"
            hit_time = pygame.time.get_ticks()
            speed = 0
            player_can_move = False

    elif ghost_state == "hit":
        if pygame.time.get_ticks() - hit_time > 1000:
            ghost_state = "fading"

    elif ghost_state == "fading":
        ghost_alpha -= 3
        if ghost_alpha <= 0:
            ghost_alpha = 0
            ghost_state = "gone"
            player_can_move = True  # กลับมาขยับได้อีกครั้ง

    # === วาดทุกอย่าง ===
    screen.fill(white)
    screen.blit(BGf0, BGf0_rect)
    moving_sprites.draw(screen)

    # ผี
    if ghost_state != "gone":
        ghost_image = ghost_frames[direction][frame_index].copy()
        ghost_image.set_alpha(ghost_alpha)
        screen.blit(ghost_image, ghost.topleft)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()