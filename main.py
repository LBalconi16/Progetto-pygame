import pygame
from random import randint
import time
from eroe import Eroe
from cattivi import Cattivi
from boss import Boss
from sparo import Bullet


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

#dimensioni proiettili 
dim_bullet_buoni_x = 35
dim_bullet_buoni_y = 50


#colpi dei buoni
immagine_colpo_buoni = pygame.image.load("immagini-gioco\\colpo buoni.png.png")
image_proiettile_buoni = pygame.transform.rotate(immagine_colpo_buoni, 90)

lista_bullet = []
#ciclo fondamentale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            bullet_rect = pygame.Rect(eroe.posizione_eroe_x()+37, eroe.posizione_eroe_y()-31, dim_bullet_buoni_x, dim_bullet_buoni_y)
            d = Bullet(image_proiettile_buoni, bullet_rect)
            lista_bullet.append(d)
    key_pressed = pygame.key.get_pressed()
    eroe.move(key_pressed)
    for i in range(len(lista_bullet)):
        lista_bullet[i].muovi_bullet()


    
    screen.blit(sfondo, (0, 0))

    eroe.draw(screen)
    cattivi.draw(screen)
    for i in range(len(lista_bullet)):
        lista_bullet[i].disegna_bullet(screen)
    # bullet.update()
    # boss.draw(screen) 
    pygame.display.flip()
    clock.tick(60)