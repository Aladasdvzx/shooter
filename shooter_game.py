
from typing import Any
import pygame 
from random import randint

HEIGHT = 600
WIDTH = 1200

SIZE = (WIDTH,HEIGHT)

FPS = 60

lost = 0
score = 0

window = pygame.display.set_mode(SIZE)
background = pygame.transform.scale(
    pygame.image.load("galaxy.jpg"),
    SIZE 
    )
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, size, speed):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(filename), 
            size
        )    
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.rect.x <= 0:
                self.rect.x = WIDTH


    def fire(self):
        new_bullet = Bullet("bullet.png", ship.rect.centerx, ship.rect.y, (10,25), 4)
        bullets.add(new_bullet)
        fire_sound.play()

class Enemy (GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            global lost
            lost += 1
            self.rect.y = 0 
            self.rect.x = randint(10,WIDTH-60)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.kill()



pygame.mixer.init()
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.play()

pygame.font.init()
font1 = pygame.font.Font(None, 36)

bullets = pygame.sprite.Group()
fire_sound = pygame.mixer.Sound("fire.ogg")



ship = Player("rocket.png", WIDTH/2, HEIGHT-70, (50,70), 5)
enemies = pygame.sprite.Group()
enemies_num = 5

ball = pygame.sprite.Group()
ball_num = 5
for i in range(ball_num):
    ball_nuz = Enemy("asteroid.png", randint(10,WIDTH-80), 0 ,(50,55),randint(5,7))
    ball.add(ball_nuz)

for i in range(enemies_num):
    new_Enemies = Enemy("ufo.png", randint(10,WIDTH-60), 0 ,(50,55),randint(2,5))
    enemies.add(new_Enemies)

finish = False
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ship.fire()


    if not finish:

        window.blit(background, (0,0))

        ship.reset()
        ship.update()

        bullets.update()
        bullets.draw(window)


        enemies.draw(window)
        enemies.update()

        ball.draw(window)
        ball.update()

        text_lost = font1.render("Пропущено:" + str(lost) , True, (255,255,255))
        window.blit(text_lost, (0,0))

    pygame.display.update()
    clock.tick(FPS)









































