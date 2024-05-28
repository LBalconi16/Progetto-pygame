import pygame 
from pygame.locals import *

altezza = 600
larghezza = 800 
VEL = 5

dim_x = 20
dim_y = 35

class Bullet:
    def __init__(self, image, rect):
        self.image = image 
        self.rect = rect
        self.proiett = []
        self.image = pygame.transform.scale(self.image, (dim_x, dim_y))

    def muovi_bullet(self):
        self.rect.y -= VEL


    def disegna_bullet (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        