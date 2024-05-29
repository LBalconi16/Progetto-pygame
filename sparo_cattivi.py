import pygame 
from pygame.locals import *
immagine_colpo_cattivi = pygame.image.load("immagini-gioco\\colpo cattivi.png")

altezza = 600
larghezza = 800 
VEL = 5

dim_x = 20
dim_y = 20


class Bullet_nemici:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(immagine_colpo_cattivi, (dim_x, dim_y))
        self.rect = pygame.Rect(x-9, y-14, dim_x, dim_y)
        self.velocita = VEL

    def update(self):
        self.rect.y += self.velocita

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))