import pygame
import sys

WIDTH, HEIGHT = 800, 600

nav_dim_x = 575
nav_dim_y = 265

nav_x = (WIDTH//2) - (nav_dim_x//2)
nav_y = nav_dim_y//4

class Boss:
    def __init__(self):
        self.image = pygame.image.load("immagini-gioco\\nave boss.webp")
        self.image = pygame.transform.scale(self.image, (nav_dim_x, nav_dim_y))
        self.rect = pygame.Rect(nav_x, nav_y, nav_dim_x, nav_dim_y)

    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))