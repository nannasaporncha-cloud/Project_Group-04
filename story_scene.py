import pygame
from game_scene import run_game  # จบเนื้อเรื่องแล้วไปหน้าเกมจริง
WIDTH, HEIGHT = 1500, 850
def run_story(screen):
   # ตั้งชื่อหน้าต่าง
   pygame.display.set_caption("The Exorcist of Siam - Story")
   pygame.mixer.init()
   clock = pygame.time.Clock()
   # สีพื้นฐาน
   WHITE = (255, 255, 255)
   BLACK = (0, 0, 0)
   DARK_RED = (80, 0, 0)
   # ฟอนต์
   thai_font = "assets/THsarabaneiei.ttf"
   font = pygame.font.Font(thai_font, 48 )
   hint = pygame.font.Font(thai_font, 22 )

   # โหลดรูป
   car_bg = pygame.image.load("assets/story1_accident.png")
   car_bg = pygame.transform.scale(car_bg, (WIDTH, HEIGHT))
   white_bg = pygame.image.load("assets/story2.png")
   white_bg = pygame.transform.scale(white_bg, (WIDTH, HEIGHT))
   town_bg = pygame.image.load("assets/story3_reborn.png")
   town_bg = pygame.transform.scale(town_bg, (WIDTH, HEIGHT))
   # โหลดเสียง 
   horn_sound = pygame.mixer.Sound("assets/car_horn.mp3")
   horn_sound.set_volume(0.6)
   pygame.mixer.music.load("assets/bgm_creepy.mp3")
   
   # STORY 1: รถจะชน

   horn_sound.play(-1)   # เล่นเสียงแตรวน
   in_scene1 = True
   while in_scene1:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               horn_sound.stop()
               return
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                   horn_sound.stop()
                   in_scene1 = False    # ไปฉาก 2
       # วาดฉากรถจะชน
       screen.blit(car_bg, (0, 0))
       # ข้อความบอกผู้เล่น
       text = font.render("เห้ยยยยย ไอหนูหลบไป!!!...", True, WHITE)
       screen.blit(text, (120, HEIGHT - 140))
       pygame.display.flip()
       clock.tick(60)

   # STORY 2: ฉากขาวเงียบ เห้ยที่ไหนว้ะ
   in_scene2 = True
   while in_scene2:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                   in_scene2 = False    # ไปฉาก 3
       # ใช้รูปฉากขาวแทน fill
       screen.blit(white_bg, (0, 0))
       text = font.render("...อืม...", True, BLACK)
       hint = font.render("ที่นี่...ที่ไหน", True, BLACK)
       screen.blit(
           text,
           (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 30)
       )
       screen.blit(
           hint,
           (WIDTH // 2 - hint.get_width() // 2, HEIGHT // 2 + 10)
       )
       pygame.display.flip()
       clock.tick(60)
   
   #  STORY 3: เมืองเก่า + กล่อง dialog 
   pygame.mixer.music.set_volume(0.2)
   pygame.mixer.music.play(-1)   # เพลงหลอนวนไป
   dialog_lines = [
    
       "สมชาย: เมื่อกี้ฉันยังยืนอยู่บนถนน ทำไมถึงมาโผล่ที่นี่ได้...",
       "สมชาย: แล้วชุดนี่อะไร... ทำไมฉันแต่งตัวเหมือนหมอผีโบราณ...",
       "สมชาย: (เสียงปริศนาดังแทรกมาแบบแผ่วๆแต่เย็นยะเยือก)",
       "ชายปริศนา: เจ้าตื่นแล้วสินะ...หมอผีสมชาย",
       "สมชาย: ห้ะ?! ตรูไปเป็นหมอผีตอนไหน",
       "ชายปริศนา: ได้ข่าวว่าฝีมือปราบวิญญาณเก่งกาจไม่เบา วันนี้ข้ามีงานให้เจ้า ",
       "สมชาย: เดี๋ยวๆๆๆๆ ฟังดูไม่ดีเลยอ่ะ งานแบบนี้มันต้องมีผีแน่ๆใช่มั้ยเนี่ย",
       "ชายปริศนา: ในบ้านร้างหลังนั้น...เจ้าต้องไปจัดการผีร้าย",
       "สมชาย: นั่นไง พูดไม่ทันขาดคำ แล้วผมจะได้ค่าตอบแทนจากงานนี้ยังไง",
       "ชายปริศนา: ฮะ ฮะ ฮะ ถ้าเจ้ารอดกลับมาได้ ค่อยคุยเรื่องนั้น",
       "สมชาย: ...โอเค สรุปคือถ้าตายก็ไม่ได้ค่าจ้าง งั้นผมขอค่าทำขวัญล่วงหน้าได้มั้ยพี่",
       "สมชาย: เอ้า หายไปแล้ว!? ",
       "สมชาย: เฮ้อ...งั้นก็เหลือแค่ฉันกับบ้านผีสิงหลังนี้สินะ...เอาวะสมชาย สู้เพื่อค่าข้าวเย็น!",

   ]
   current_line = 0
   dialog_rect = pygame.Rect(20, HEIGHT - 140, WIDTH - 40, 120)
   in_scene3 = True
   while in_scene3:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.mixer.music.stop()
               return
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                   # ยังไม่จบเนื้อเรื่อง ไปบรรทัดถัดไป
                   if current_line < len(dialog_lines) - 1:
                       current_line += 1
                   # จบบรรทัดสุดท้ายแล้ว เข้าฉากเกม
                   else:
                       pygame.mixer.music.fadeout(500)
                       in_scene3 = False
       # พื้นหลังเมืองเก่า
       screen.blit(town_bg, (0, 0))
       # กล่องข้อความ
       pygame.draw.rect(screen, WHITE, dialog_rect, border_radius=8)
       pygame.draw.rect(screen, BLACK, dialog_rect, 2, border_radius=8)
     
       line_surface = font.render(dialog_lines[current_line], True, BLACK)
       screen.blit(line_surface, (dialog_rect.x + 16, dialog_rect.y + 24))
       # hint ด้านล่าง
    
       hint_show = font.render("", True, DARK_RED)
       screen.blit(hint_show, (dialog_rect.x + 16, dialog_rect.y + dialog_rect.height - 30))
       pygame.display.flip()
       clock.tick(60)
   # จบ story แล้วเข้า game scene
   run_game(screen)
 
 