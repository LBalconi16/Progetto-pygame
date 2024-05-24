import pygame
from random import randint
import time
from eroe import Eroe
from cattivi import Cattivi
from boss import Boss

WIDTH, HEIGHT = 800, 600

#finestra base
clock = pygame.time.Clock()
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Gioco navicelle')
sfondo = pygame.image.load("immagini-gioco\\sfondo progetto.jpg")
sfondo  = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
eroe = Eroe()
cattivi = Cattivi(3, 12)
boss = Boss()
#ciclo fondamentale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = pygame.key.get_pressed()
    eroe.move(key_pressed)
    screen.blit(sfondo, (0, 0))
    eroe.draw(screen)
    cattivi.draw(screen)
    #boss.draw(screen) -> quando gli scagnozzi sono morti
    pygame.display.flip()
    clock.tick(60)