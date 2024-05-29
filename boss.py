import pygame
import sys
from sparo_boss import Bullet_boss
import random

WIDTH, HEIGHT = 800, 600

nav_dim_x = 575
nav_dim_y = 265

#vita boss
vita_boss = 100
nav_x = (WIDTH//2) - (nav_dim_x//2)
nav_y = nav_dim_y//4

class Boss:
    def __init__(self):
        self.image = pygame.image.load("immagini-gioco\\nave boss.webp")
        self.image = pygame.transform.scale(self.image, (nav_dim_x, nav_dim_y))
        self.rect = pygame.Rect(nav_x, nav_y, nav_dim_x, nav_dim_y)
        self.proiettili = []

    
    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        for proiettile in self.proiettili:
            proiettile.draw(screen)
    
    def update(self):
        prob1 = random.randint(1, 25)
        if prob1 == 10:
            self.spara()
        for proiettile in self.proiettili:
            proiettile.update()
    
    def spara(self):
        x1 = self.rect.x + 20
        x2 = self.rect.x + nav_dim_x//2
        x3 = self.rect.x +nav_dim_x -20
        y1 = self.rect.y + 50
        y2 = self.rect.y +nav_dim_y
        y3 = self.rect.y + 50
        self.proiettili.append(Bullet_boss(x1, y1))
        self.proiettili.append(Bullet_boss(x2, y2))
        self.proiettili.append(Bullet_boss(x3, y3))
