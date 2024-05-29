import pygame 
from pygame.locals import *
import random
immagine_colpo_boss = pygame.image.load("immagini-gioco\\colpo_del_boss.png")

altezza = 600
larghezza = 800 
VEL = 5

dim_x = 80
dim_y = 60




class Bullet_boss:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(immagine_colpo_boss, (dim_x, dim_y))
        self.rect = pygame.Rect(x, y, dim_x, dim_y)
        self.velocita = VEL
        

    def update(self):
        self.rect.y += self.velocita
        prob = random.randint(-10, 9)
        self.rect.x += prob


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))