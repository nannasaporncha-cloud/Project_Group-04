import pygame, random, os
from player import player, moving_sprites
from setting import screen, clock, BGf0, BGf0_rect, white, fps

pygame.display.set_caption("Exorcist")

# โหลดภาพผี
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
    ghost_frames[d] = [pygame.transform.scale(img,(100,100)) for img in ghost_frames[d]]

# สร้างโซนสี่เหลี่ยม 4 โซน
zone1 = pygame.Rect(100,100,300,300)
zone2 = pygame.Rect(500,100,300,300)
zone3 = pygame.Rect(100,450,300,300)
zone4 = pygame.Rect(500,450,300,300)

zones = [zone1, zone2, zone3, zone4]

# สุ่มสร้างผี 4 ตัว
ghosts = []
for zone in zones:
    g = {
        "rect": pygame.Rect(
            random.randint(zone.left, zone.right),
            random.randint(zone.top, zone.bottom),
            50, 120
        ),
        "room": zone,
        "speed": random.randint(2,5),
        "frame_index": 0,
        "frame_timer": 0,
        "direction": "right",
        "state": "active",
        "alpha": 150,
        "hp": random.randint(5,8),
        "target": [
            random.randint(zone.left, zone.right),
            random.randint(zone.top, zone.bottom)
        ]
    }
    ghosts.append(g)


# ผีเคลื่อนที่
def move_random(g):
    if abs(g["rect"].x - g["target"][0]) < 5 and abs(g["rect"].y - g["target"][1]) < 5:
        g["target"] = [
            random.randint(g["room"].left, g["room"].right),
            random.randint(g["room"].top, g["room"].bottom)
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


# Game Loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # player attack
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

    # update player
    player.update()

    # update ghosts
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

    # detect attack hit
    pygame.mixer.init()
    death_sound = pygame.mixer.Sound(os.path.join("image_enemy/ghost_sound.mp3"))
    death_sound.set_volume(0.5)

    if attack:
        for g in ghosts:
            if g["state"] == "active" and attack_rect.colliderect(g["rect"]):
                g["hp"] -= 1
                if g["hp"] <= 0:
                    g["state"] = "fading"
                    death_sound.play()

    # draw everything
    screen.fill(white)
    screen.blit(BGf0, BGf0_rect)
    moving_sprites.draw(screen)

    # draw all ghosts
    for g in ghosts:
        if g["state"] != "gone":
            img = ghost_frames[g["direction"]][g["frame_index"]].copy()
            img.set_alpha(g["alpha"])
            screen.blit(img, g["rect"].topleft)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()