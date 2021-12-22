# -*- coding: cp1251 -*-
import pygame
import os
import random
import time
import sys
sys.setrecursionlimit(10000)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
WIDTH = 480
HEIGHT = 680
FPS = 60
running = True
heat = 2
player_hp = 3  #hp herous
opt = [list(i) for i in input().split()] #-сложность уровня задает хначение кол во нло
#  значение цветов (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):  # игрок (самолет)

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
        if self.rect.right > WIDTH:  # проверка что бы за зону не выходил
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

count = 0
class Agro(pygame.sprite.Sprite):  # агро школьница (камень)
    count += 1
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
            all_sprites.update()
            s = gm()
            all_sprites.add(s)
            m = button_play_stop()
            all_sprites.add(m)
           # all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(1)
            #running = False



    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)



class Bullet(pygame.sprite.Sprite):  # патрон для самолета
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


class gm(pygame.sprite.Sprite):  # фон
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gm_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

class button_play_stop (pygame.sprite.Sprite):  # фон
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = butt_pl
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2 - 100


class hp (pygame.sprite.Sprite):  # кол во хп
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


class hp_kol_vo (pygame.sprite.Sprite):  # кол во хп
    def __init__(self, x):
        global qw
        global s
        pygame.sprite.Sprite.__init__(self)
        if x == 2:
            s = 2
            self.image = two_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 60
        elif x == 1:
            if s == 2 and x == 1:
                qw = 1
            self.image = one_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 60
        else:
            s = 2
            if s == 2:
                qw = 1
            self.image = zero_img
            self.rect = self.image.get_rect()
            self.rect.centerx = 120
            self.rect.bottom = 60

    def update(self):
        global qw
        if qw == 1:
            print(qw)
            self.rect.centerx = 1200
            qw = 0



pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # задает дисплею высоту и ширина
pygame.display.set_caption('dior')  # задает название приложения имя
clock = pygame.time.Clock()  # надо чтобы убедиться в fps

butt_pl = pygame.image.load(os.path.join(img_folder, 'butt_pl.png')).convert_alpha()
player_img = pygame.image.load(os.path.join(img_folder, 'plane4.png')).convert_alpha()
ct_img = pygame.image.load(os.path.join(img_folder, 'tone.png')).convert_alpha()
pl_img = pygame.image.load(os.path.join(img_folder, 'w.png')).convert_alpha()
gm_img = pygame.image.load(os.path.join(img_folder, 'gm1.png')).convert_alpha()
fon_img = pygame.image.load(os.path.join(img_folder, 'fon.png')).convert_alpha()
hp_img = pygame.image.load(os.path.join(img_folder, 'hp.png')).convert_alpha()

# цифры
one_img = pygame.image.load(os.path.join(img_folder, 'one.png')).convert_alpha()
two_img = pygame.image.load(os.path.join(img_folder, 'two.png')).convert_alpha()
zero_img = pygame.image.load(os.path.join(img_folder, 'zero.png')).convert_alpha()




agros = pygame.sprite.Group()
bullets = pygame.sprite.Group()
kol_vo = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
#agros.add(m)

for i in (list(opt)):
    m = Agro()
    all_sprites.add(m)
    agros.add(m)

m = hp()
all_sprites.add(m)
# Цикл игры
while running:
    clock.tick(FPS)
    all_sprites.update()
    for event in pygame.event.get():  # различные ивенты
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_1:
                FPS = 0.5
            elif event.key == pygame .K_2:
                FPS = 60
    # Ввод процесса (события)

    hits = pygame.sprite.groupcollide(agros, bullets, True, True)
    for hit in hits:
        m = Agro()
        all_sprites.add(m)
        agros.add(m)

    # Проверка, не ударил ли  моб игрока
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
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    # Визуализация (сборка)
pygame.quit()
