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
        self.rect = pygame.Rect(nav_x, nav_y, nav_dim_x, nav_dim_y)
        self.figura_colpita1a = pygame.Rect(nav_x+35, nav_y, nav_dim_x-35, 120)
        self.figura_colpita2a = pygame.Rect(nav_x+265, nav_y+120, 65, 130)
        self.figura_colpita1b = pygame.Rect(266, nav_y, 421, 120)
        self.figura_colpita2b = pygame.Rect(nav_x+265, nav_y+120, 65, 130)
        self.figura_colpita1c = pygame.Rect(266, nav_y, 278, 120)
        self.figura_colpita2c = pygame.Rect(nav_x+265, nav_y+120, 65, 130)
        self.proiettili = []

    
    def draw (self, screen, image, vita):
        if vita>=67:
            image = pygame.transform.scale(image, (nav_dim_x, nav_dim_y))
            rect = pygame.Rect(nav_x, nav_y, nav_dim_x, nav_dim_y)
        elif vita>=34:
            image = pygame.transform.scale(image, (421, nav_dim_y))
            rect = pygame.Rect(266, nav_y, 421, nav_dim_y)
        else:
            image = pygame.transform.scale(image, (278, nav_dim_y))
            rect = pygame.Rect(266, nav_y, 278, nav_dim_y)
        screen.blit(image, (rect.x, rect.y))
        for proiettile in self.proiettili:
            proiettile.draw(screen)
    
    def update(self, vita_boss):
        prob1 = random.randint(1, 30)
        if prob1 == 10:
            self.spara(vita_boss)
        for proiettile in self.proiettili:
            proiettile.update()
    
    def spara(self, vita_boss):
        if vita_boss >=67:
            x1 = self.rect.x + 20
            x2 = self.rect.x + nav_dim_x//2-30
            x3 = self.rect.x +nav_dim_x 
            y1 = self.rect.y + 50
            y2 = self.rect.y +nav_dim_y
            y3 = self.rect.y + 50
            self.proiettili.append(Bullet_boss(x1, y1))
            self.proiettili.append(Bullet_boss(x2, y2))
            self.proiettili.append(Bullet_boss(x3, y3))
                
        elif vita_boss>=34:
            x2 = self.rect.x + nav_dim_x//2-30
            x3 = self.rect.x +nav_dim_x -20
            y2 = self.rect.y +nav_dim_y
            y3 = self.rect.y + 50
            self.proiettili.append(Bullet_boss(x2, y2))
            self.proiettili.append(Bullet_boss(x3, y3))
        else:           
            x2 = self.rect.x + nav_dim_x//2-30
            y2 = self.rect.y +nav_dim_y
            self.proiettili.append(Bullet_boss(x2, y2))
