# -*- coding: cp1251 -*-
import pygame
import os
import random
import time

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
WIDTH = 480
HEIGHT = 680
FPS = 60
running = True
heat = 10
player_hp = 3  #hp herous
opt = input()
#  ???????? ?????? (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):  # ????? (???????)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        n = 4
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.speedx = -n
            self.rect.y += self.speedx
        if keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.speedx = n
            self.rect.y += self.speedx
        if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.speedx = -n
            self.rect.x += self.speedx
        if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.speedx = n
            self.rect.x += self.speedx
        if self.rect.right > WIDTH:  # ???????? ??? ?? ?? ???? ?? ???????
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        elif self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Agro(pygame.sprite.Sprite):  # ???? ????????? (??????)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ct_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 8)
        self.speedx = random.randrange(-1, 2)
       # if random.randint(0, 2) == 1:
        #    self.shoot()
         #   print(1)

    def update(self):
        global heat
        global running
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        #print(self.rect.y)
        if self.rect.y > 680:
            heat -= 1
            q = hp_kol_vo(heat)
            all_sprites.add(q)
            print(heat)
            self.rect.bottom = 0
        if heat < 1:
            s = gm()
            all_sprites.add(s)
            m = button_play_stop()
            all_sprites.add(m)
           # all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(5)
            #running = False



    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)



class Bullet(pygame.sprite.Sprite):  # ?????? ??? ????????
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 10
        self.image = pl_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class gm(pygame.sprite.Sprite):  # ???
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

class button_play_stop (pygame.sprite.Sprite):  # ???
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = butt_pl
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2 - 100


class hp (pygame.sprite.Sprite):  # ??? ?? ??
    def __init__(self):
        print(heat)
        pygame.sprite.Sprite.__init__(self)
        q = hp_kol_vo(heat)
        all_sprites.add(q)
        self.image = hp_img
        self.rect = self.image.get_rect()
        self.rect.centerx = 70
        self.rect.bottom = 60

qw = 0
s = 0


class hp_kol_vo (pygame.sprite.Sprite):  # ??? ?? ??
    def __init__(self, x):
        global qw
        global s
        pygame.sprite.Sprite.__init__(self)
        if x == 10:
            s = 2
            self.image = ten_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 140
            self.rect.bottom = 70
        elif x == 9:
            if s == 2 and x == 9:
                qw = 1
            s = 2
            self.image = nine_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 70
        elif x == 8:
            if s == 2 and x == 8:
                qw = 1
            s = 2
            self.image = eig_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 130
            self.rect.bottom = 80
        elif x == 7:
            if s == 2 and x == 7:
                qw = 1
            s = 2
            self.image = sev_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 75
        elif x == 6:
            if s == 2 and x == 6:
                qw = 1
            s = 2
            self.image = six_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 70
        elif x == 5:
            if s == 2 and x == 5:
                qw = 1
            s = 2
            self.image = fif_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 70
        elif x == 4:
            if s == 2 and x == 4:
                qw = 1
            s = 2
            self.image = four_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 80
        elif x == 3:
            if s == 2 and x == 3:
                qw = 1
            s = 2
            self.image = thr_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 85
        elif x == 2:
            if s == 2 and x == 2:
                qw = 1
            s = 2
            self.image = two_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 65
        elif x == 1:
            if s == 2 and x == 1:
                qw = 1
            self.image = one_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 65
        else:
            s = 2
            if s == 2:
                qw = 1
            self.image = zero_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 65

    def update(self):
        global qw
        if qw == 1:
            print("-------------------------")
            self.rect.centerx = 12000
            self.kill()
            #print(self)
            qw = 0



pygame.init()  # ?????? pygame
pygame.mixer.init()  # ?????? ?????
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # ?????? ??????? ?????? ? ??????
pygame.display.set_caption('dior')  # ?????? ???????? ?????????? ???
clock = pygame.time.Clock()  # ???? ????? ????????? ? fps

butt_pl = pygame.image.load(os.path.join(img_folder, 'butt_pl.png')).convert_alpha()
player_img = pygame.image.load(os.path.join(img_folder, 'plane4.png')).convert_alpha()
ct_img = pygame.image.load(os.path.join(img_folder, 'tone.png')).convert_alpha()
pl_img = pygame.image.load(os.path.join(img_folder, 'w.png')).convert_alpha()
gm_img = pygame.image.load(os.path.join(img_folder, 'gm1.png')).convert_alpha()
fon_img = pygame.image.load(os.path.join(img_folder, 'fon.png')).convert_alpha()
hp_img = pygame.image.load(os.path.join(img_folder, 'hp.png')).convert_alpha()

# ?????
one_img = pygame.image.load(os.path.join(img_folder, 'one.png')).convert_alpha()
two_img = pygame.image.load(os.path.join(img_folder, 'two.png')).convert_alpha()
zero_img = pygame.image.load(os.path.join(img_folder, 'zero.png')).convert_alpha()
thr_img = pygame.image.load(os.path.join(img_folder, 'three.png')).convert_alpha()
four_img = pygame.image.load(os.path.join(img_folder, 'four.png')).convert_alpha()
fif_img = pygame.image.load(os.path.join(img_folder, 'fif.png')).convert_alpha()
six_img = pygame.image.load(os.path.join(img_folder, 'six.png')).convert_alpha()
sev_img = pygame.image.load(os.path.join(img_folder, 'sev.png')).convert_alpha()
eig_img = pygame.image.load(os.path.join(img_folder, 'eig.png')).convert_alpha()
nine_img = pygame.image.load(os.path.join(img_folder, 'nine.png')).convert_alpha()
ten_img = pygame.image.load(os.path.join(img_folder, 'ten.png')).convert_alpha()





agros = pygame.sprite.Group()
bullets = pygame.sprite.Group()
kol_vo = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#agros.add(m)

m = Agro()
all_sprites.add(m)
agros.add(m)

m = hp()
all_sprites.add(m)
# ???? ????
while running:
    clock.tick(FPS)
    all_sprites.update()
    for event in pygame.event.get():  # ????????? ??????
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_1:
                FPS = 0.5
            elif event.key == pygame .K_2:
                FPS = 60
    # ???? ???????? (???????)

    hits = pygame.sprite.groupcollide(agros, bullets, True, True)
    for hit in hits:
        m = Agro()
        all_sprites.add(m)
        agros.add(m)

    # ????????, ?? ?????? ??  ??? ??????
    hits = pygame.sprite.spritecollide(player, agros, False)
   # if hits:
       # s = 0
       # if s == 0:
       #     print(player_hp)
        #    player_hp -= 1
        #    if player_hp == 0:
        #        s = gm()
          #      all_sprites.add(s)
          #      agros.add(s)
            # all_sprites.draw(screen)
            # pygame.display.flip()
             #   running = False
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # ????? ????????? ?????, ?????????????? ?????
    pygame.display.flip()
    # ???????????? (??????)
pygame.quit()
