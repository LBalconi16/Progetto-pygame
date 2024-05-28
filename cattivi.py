import pygame
import random
from sparo_cattivi import Bullet_nemici
WIDTH, HEIGHT = 800, 600
class Cattivi:
    def __init__(self, righe, colonne):
        self.nemici = []
        self.nemici2 = []
        self.larghezza = 50
        self.altezza = 50
        self.image = pygame.image.load("immagini-gioco\\immagine cattivo mini.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (self.larghezza, self.altezza))
        self.righe = righe
        self.colonne = colonne
        self.proiettili = []
        self.nemici_sconfitti = False
        self.crea_nemici()   
    def crea_nemici(self):
        margine = 10
        distanzax = (WIDTH - (self.colonne * self.larghezza + (self.colonne - 1) * margine)) // 2
        distanzay = 50
        for riga in range(self.righe):
            for colonna in range(self.colonne):
                x = distanzax + colonna * (self.larghezza + margine)
                y = distanzay + riga * (self.altezza + margine)
                self.nemici2.append((riga+1)*(colonna+1))
                self.nemici.append(pygame.Rect(x, y, self.larghezza, self.altezza))

    def draw(self, screen):
        for nemico in self.nemici:
            screen.blit(self.image, (nemico.x, nemico.y))
        for proiettile in self.proiettili:
            proiettile.draw(screen)
    def update(self):
        prob1 = random.randint(1, 25)
        if prob1 == 10:
            self.spara()

        # Aggiorna la posizione dei proiettili
        for proiettile in self.proiettili:
            proiettile.update()
        if len(self.nemici) == 0:
            self.nemici_sconfitti = True
        
    def spara(self):
        if self.nemici:
            prob2 = random.randint(0, len(self.nemici) - 1)  
            nemico = self.nemici[prob2] 
            x = nemico.x + self.larghezza // 2
            y = nemico.y + self.altezza
            self.proiettili.append(Bullet_nemici(x, y))
            