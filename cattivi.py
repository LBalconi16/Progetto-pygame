import pygame
import random
WIDTH, HEIGHT = 800, 600
class Cattivi:
    def __init__(self, righe, colonne):
        self.nemici = []
        self.larghezza = 50
        self.altezza = 50
        self.image = pygame.image.load("immagini-gioco\\immagine cattivo mini.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (self.larghezza, self.altezza))
        self.righe = righe
        self.colonne = colonne
        self.crea_nemici()   
    def crea_nemici(self):
        margine = 10
        distanzax = (WIDTH - (self.colonne * self.larghezza + (self.colonne - 1) * margine)) // 2
        distanzay = 50
        for riga in range(self.righe):
            for colonna in range(self.colonne):
                x = distanzax + colonna * (self.larghezza + margine)
                y = distanzay + riga * (self.altezza + margine)
                self.nemici.append(pygame.Rect(x, y, self.larghezza, self.altezza))

    def draw(self, screen):
        for nemico in self.nemici:
            screen.blit(self.image, (nemico.x, nemico.y))
            