import pygame, random, os
from player import player, moving_sprites
from setting import screen, clock, BGf0, BGf0_rect, white, fps

# โหลดภาพผี (ปัญญาประดิษฐ์)
ghost_frames = {
    "right": [
        pygame.image.load(os.path.join("image_enemy/ghost1.png")).convert_alpha(),
        pygame.image.load(os.path.join("image_enemy/ghost2.png")).convert_alpha()
    ],
    "left": [
        pygame.image.load(os.path.join("image_enemy/ghost3.png")).convert_alpha(),
        pygame.image.load(os.path.join("image_enemy/ghost4.png")).convert_alpha()
    ],
    "up": [
        pygame.image.load(os.path.join("image_enemy/ghost1.png")).convert_alpha(),
        pygame.image.load(os.path.join("image_enemy/ghost2.png")).convert_alpha()
    ],
    "down": [
        pygame.image.load(os.path.join("image_enemy/ghost3.png")).convert_alpha(),
        pygame.image.load(os.path.join("image_enemy/ghost4.png")).convert_alpha()
    ]
}

for d in ghost_frames:
    ghost_frames[d] = [pygame.transform.scale(img,(80,80)) for img in ghost_frames[d]]

# สร้างโซนสี่เหลี่ยม 4 โซน (ศึกษาเองจาก https://www.youtube.com/watch?v=SpQHJgJi7mk)
zone1 = pygame.Rect(100,100,300,300)
zone2 = pygame.Rect(500,100,300,300)
zone3 = pygame.Rect(100,450,300,300)
zone4 = pygame.Rect(500,450,300,300)

zones = [zone1, zone2, zone3, zone4]

# สุ่มสร้างผี 4 ตัว (ปัญญาประดิษฐ์ ยกเว้น random.randrange ศึกษาจาก Lab 7 ข้อที่ 5)
ghosts = []
for zone in zones:
    g = {
        "rect": pygame.Rect(
            random.randrange(zone.left, zone.right),
            random.randrange(zone.top, zone.bottom),
            50, 120
        ),
        "room": zone,
        "speed": random.randrange(2,5),
        "frame_index": 0,
        "frame_timer": 0,
        "direction": "right",
        "state": "active",
        "alpha": 150,
        "hp": random.randint(5,8),
        "target": [
            random.randrange(zone.left, zone.right),
            random.randrange(zone.top, zone.bottom)
        ]
    }
    ghosts.append(g)


# ผีเคลื่อนที่ (ปัญญาประดิษฐ์)
def move_random(g):
    if abs(g["rect"].x - g["target"][0]) < 5 and abs(g["rect"].y - g["target"][1]) < 5:
        g["target"] = [
            random.randrange(g["room"].left, g["room"].right),
            random.randrange(g["room"].top, g["room"].bottom)
        ]

    dx = g["target"][0] - g["rect"].x
    dy = g["target"][1] - g["rect"].y

    if dx > 0: g["rect"].x += g["speed"]
    elif dx < 0: g["rect"].x -= g["speed"]

    if dy > 0: g["rect"].y += g["speed"]
    elif dy < 0: g["rect"].y -= g["speed"]

    if dx > 0: g["direction"] = "right"
    elif dx < 0: g["direction"] = "left"


def chase_player(g):
    dx = player.rect.centerx - g["rect"].centerx
    dy = player.rect.centery - g["rect"].centery

    if dx > 0: g["rect"].x += g["speed"]
    elif dx < 0: g["rect"].x -= g["speed"]

    if dy > 0: g["rect"].y += g["speed"]
    elif dy < 0: g["rect"].y -= g["speed"]

    if dx > 0: g["direction"] = "right"
    elif dx < 0: g["direction"] = "left"


def keep_inside(g):
    r = g["rect"]
    room = g["room"]

    if r.left < room.left: r.left = room.left
    if r.right > room.right: r.right = room.right
    if r.top < room.top: r.top = room.top
    if r.bottom > room.bottom: r.bottom = room.bottom


# Game Loop (ปัญญาประดิษฐ์)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # player attack (ปัญญาประดิษฐ์ ยกเว้น เงื่อนไขใน if ของ player attack ศึกษาแล้วนำมาจาก player.py แต่ไม่ใช่ attack_rect)
    attack = False
    attack_rect = None
    if keys[pygame.K_SPACE]:
        attack = True
        if keys[pygame.K_a]:  
            new_dir = 'attackL'
            attack_rect = pygame.Rect(player.rect.left-40, player.rect.centery-20, 40, 40)
        elif keys[pygame.K_d] :  
            new_dir = 'attackR'
            attack_rect = pygame.Rect(player.rect.right, player.rect.centery-20, 40, 40)

    player.update()

    # update ghosts (ปัญญาประดิษฐ์)
    for g in ghosts:
        if g["state"] == "active":
            if g["room"].collidepoint(player.rect.center):
                chase_player(g)
            else:
                move_random(g)

            keep_inside(g)

            g["frame_timer"] += 1
            if g["frame_timer"] >= 15:
                g["frame_timer"] = 0
                g["frame_index"] = (g["frame_index"] + 1) % len(ghost_frames[g["direction"]])

        elif g["state"] == "fading":
            g["alpha"] -= 3
            if g["alpha"] <= 0:
                g["state"] = "gone"
                g["alpha"] = 0

    # detect attack hit (ปัญญาประดิษฐ์ ยกเว้น sound ศึกษามาจาก https://www.youtube.com/watch?v=n1mKIK7lCx0)
    pygame.mixer.init()
    death_sound = pygame.mixer.Sound("image_enemy/ghost_sound.mp3")

    if attack:
        for g in ghosts:
            if g["state"] == "active" and attack_rect.colliderect(g["rect"]):
                g["hp"] -= 1
                if g["hp"] <= 0:
                    g["state"] = "fading"
                    pygame.mixer.Sound.play(death_sound)

    # draw everything (ปัญญาประดิษฐ์)
    screen.fill(white)
    screen.blit(BGf0, BGf0_rect)
    moving_sprites.draw(screen)

    # draw all ghosts (ปัญญาประดิษฐ์)
    for g in ghosts:
        if g["state"] != "gone":
            img = ghost_frames[g["direction"]][g["frame_index"]].copy()
            img.set_alpha(g["alpha"])
            screen.blit(img, g["rect"].topleft)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()