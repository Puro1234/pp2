import pygame
import random
import time
from pygame.locals import *

pygame.init()

#Frames per second
clock = pygame.time.Clock()


#Colors 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Font
font_small = pygame.font.SysFont("Verdana", 20)

#Images
player_img = pygame.image.load("Player.png")
enemy_img = pygame.image.load("Enemy.png")
background_img = pygame.image.load("AnimatedStreet.png")
gameover_img = pygame.image.load("gameover.jpg")
gameover_img = pygame.transform.scale(gameover_img, (350, 281))

#Sounds:
crash_sound = pygame.mixer.Sound("crash.wav")
background_song = pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)


#Screen
w, h = 400, 600
screen = pygame.display.set_mode((w, h))
screen.blit(background_img, (0, 0))

#Speeds
player_speed = 5
enemy_speed = 6

#Score var
score = 0

#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = w // 2 - self.rect.w // 2
        self.rect.y = h - self.rect.h 
    
    def moving(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-player_speed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(player_speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > w:
            self.rect.right = w

    

        
#Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.random_rect()

    def moving(self):
        global score
        self.rect.move_ip(0, enemy_speed)
        if self.rect.bottom > h:
            score += 1
            self.random_rect()

    def random_rect(self):
        self.rect.x = random.randint(0, w - self.rect.w)
        self.rect.y = 0

#Sprites
player = Player()
enemy = Enemy()

#Grouping sprites
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add([player, enemy])
enemy_sprites.add([enemy])

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            enemy_speed += 1
        if event.type == QUIT:
            pygame.quit()

    screen.blit(background_img, (0, 0))
    scores = font_small.render(str(score), True, BLACK)
    screen.blit(scores, (10, 10))

    player.moving()
    enemy.moving()

    for sprt in all_sprites:
        screen.blit(sprt.image, sprt.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
     pygame.mixer.music.stop()  
     crash_sound.play()
     time.sleep(1.5)
 
     screen.fill(WHITE)
     screen.blit(gameover_img, (25, 100))
     pygame.display.flip()

     time.sleep(2)

     running = False


    pygame.display.flip()
    clock.tick(60)