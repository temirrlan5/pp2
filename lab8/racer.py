import pygame 
import random 
import time 

from pygame.locals import * 
from pygame import mixer 

# Constants 
WIDTH = 600 
HEIGHT = 500 

BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
BLUE = (0, 0, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 

# Display 
pygame.init() 
pygame.display.set_caption("Endless Ride 1") 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
bg = pygame.Surface((WIDTH, HEIGHT)) 
road = pygame.Surface((300, HEIGHT)) 
clock = pygame.time.Clock() 
road.fill((79, 81, 78)) 
bg.fill((76, 169, 5)) 
done = False 

# Game variables 
coins = 0 
score = 0 
speed = 1 

# Fonts
font = pygame.font.SysFont("Verdana", 90) 
font_small = pygame.font.SysFont("Verdana", 22) 
game_over = font.render("Game Over", True, RED) 
text_rect = game_over.get_rect(center=(WIDTH / 2, HEIGHT / 2)) 

# Background sound 
mixer.init()  # Initialize mixer
mixer.music.load("media/background2.mp3") 
mixer.music.play(-1) 

# Images
coin_image = pygame.image.load('image/coin.png') 
flowers_image = pygame.image.load('image/pink_flower.png') 

# Classes
class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load('image/car2.png') 
        self.lives = 3 
        self.hidden = False 
        self.hide_timer = pygame.time.get_ticks() 
        self.rect = self.image.get_rect(center=(250, 400)) 

    def move(self): 
        pressed_keys = pygame.key.get_pressed() 

        if self.rect.top > 0: 
            if pressed_keys[K_UP]: 
                self.rect.move_ip(0, -5) 
        if self.rect.bottom < 480: 
            if pressed_keys[K_DOWN]: 
                self.rect.move_ip(0, 5) 

        if self.rect.left > 155: 
            if pressed_keys[K_LEFT]: 
                self.rect.move_ip(-5, 0) 
        if self.rect.right < 435: 
            if pressed_keys[K_RIGHT]: 
                self.rect.move_ip(5, 0) 

    def hide(self): 
        self.hidden = True 
        self.hide_timer = pygame.time.get_ticks() 
        self.rect.center = (WIDTH / 2, HEIGHT - 70) 

    def update(self): 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000: 
            self.hidden = False 
            self.rect.center = (WIDTH / 2, HEIGHT - 70) 

class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load('image/enemy2.png') 
        self.rect = self.image.get_rect(center=(random.randint(180, 400), 0)) 

    def move(self): 
        global score 
        self.rect.move_ip(0, random.randint(speed, 5)) 
        if self.rect.bottom > HEIGHT: 
            self.rect.top = 0 
            self.rect.center = (random.randint(180, 400), 0) 

# Initialize sprites
P1 = Player() 
E1 = Enemy() 

obstacles = [] 
enemies = pygame.sprite.Group() 
enemies.add(E1) 
all_sprites = pygame.sprite.Group() 
all_sprites.add(P1) 
all_sprites.add(E1) 

# Main game loop
while not done: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            done = True 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
            done = True 

    screen.blit(bg, (0, 0)) 
    screen.blit(road, (150, 0)) 

    # Game logic

    # Drawing

    pygame.display.update() 
    clock.tick(60) 

pygame.quit()
