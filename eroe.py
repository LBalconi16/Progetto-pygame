import pygame

WIDTH, HEIGHT = 800, 600
VEL = 5

dim_nav_x, dim_nav_y = 100, 100
nav_x, nav_y = (WIDTH // 2) - (dim_nav_x // 2), HEIGHT - dim_nav_y

class Eroe:
    def __init__(self):
        self.image = pygame.image.load("immagini-gioco\\nave buoni.webp")
        self.image = pygame.transform.scale(self.image, (dim_nav_x, dim_nav_y))
        self.rect = pygame.Rect(nav_x, nav_y, dim_nav_x, dim_nav_y)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_a] and self.rect.x >= 0:
            self.rect.x -= VEL
        if keys[pygame.K_d] and self.rect.x <= WIDTH - self.rect.width:
            self.rect.x += VEL
        if keys[pygame.K_w] and self.rect.y >= 0:
            self.rect.y -= VEL
        if keys[pygame.K_s] and self.rect.y <= HEIGHT - self.rect.height:
            self.rect.y += VEL

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))