import pygame
import random
WIDTH, HEIGHT = 800, 600
class Cattivi:
    def __init__(self, num_nemici):
        self.nemici = []
        self.larghezza = 50
        self.altezza = 50
        self.image = pygame.image.load("immagini-gioco\\nave piccolo cattivo.png")
        self.image = pygame.transform.scale(self.image, (self.larghezza, self.altezza))
        for i in range(num_nemici):
            x = random.randint(0, WIDTH - self.larghezza)
            y = random.randint(0, HEIGHT // 3)
            self.nemici.append(pygame.Rect(x, y, self.larghezza, self.altezza))
    def draw(self, screen):
        for nemico in self.nemici:
            screen.blit(self.image, (nemico.x, nemico.y))