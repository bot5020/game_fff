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
heat = 20

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


class Agro(pygame.sprite.Sprite):  # агро школьница (камень)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ct_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 8)
        self.speedx = random.randrange(-1, 2)

    def update(self):
        if self.rect.bottom == 0: print(self.rect.bottom)
        global heat
        global running
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

        if self.rect.y == 0:
            g = 1
            if g == 1:
                heat -= 1
                print(heat)
            self.rect.bottom = 0
        if heat < 1:
            s = gm()
            all_sprites.add(s)
            Agro.add(s)
            all_sprites.draw(screen)
            pygame.display.flip()
            time.sleep(3)
            running = False


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


class gm (pygame.sprite.Sprite):  # патрон для самолета
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedy = +10
        self.speedx = 10
        self.image = gm_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


pygame.init()  # запуск pygame
pygame.mixer.init()  # запуск звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # задает дисплею высоту и ширина
pygame.display.set_caption('super game')  # задает название приложения имя
clock = pygame.time.Clock()  # надо чтобы убедиться в fps


player_img = pygame.image.load(os.path.join(img_folder, 'plane4.png')).convert_alpha()
ct_img = pygame.image.load(os.path.join(img_folder, 'tone.png')).convert_alpha()
pl_img = pygame.image.load(os.path.join(img_folder, 'w.png')).convert_alpha()
gm_img = pygame.image.load(os.path.join(img_folder, 'gm.png')).convert_alpha()
fon = pygame.image.load(os.path.join(img_folder, 'gm.png')).convert_alpha()

agros = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for k in range(4):
    m = Agro()
    all_sprites.add(m)
    agros.add(m)


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
            elif event.key == pygame.K_h:
                FPS = 60
    # Ввод процесса (события)

    hits = pygame.sprite.groupcollide(agros, bullets, True, True)
    for hit in hits:
        m = Agro()
        all_sprites.add(m)
        agros.add(m)

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, agros, False)
    if hits:
        s = gm()
        all_sprites.add(s)
        agros.add(s)
        #all_sprites.draw(screen)
               #pygame.display.flip()
        running = False
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
    # Визуализация (сборка)
pygame.quit()
