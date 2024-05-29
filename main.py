import pygame
import random 
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
sfondo = pygame.image.load("immagini-gioco\\sfondo1.jpg")
sfondo  = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
cattiviy = 3
cattivix = 12
eroe = Eroe()
cattivi = Cattivi(cattiviy, cattivix)
boss = Boss()
FPS = 30



#dimensioni proiettili 
dim_bullet_buoni_x = 35
dim_bullet_buoni_y = 50

#dimensioni proiettili cattivi
dim_bullet_cattivi_x = 35
dim_bullet_cattivi_y = 50


#colpi dei buoni
immagine_colpo_buoni = pygame.image.load("immagini-gioco\\colpo buoni.png.png")
image_proiettile_buoni = pygame.transform.rotate(immagine_colpo_buoni, 90)

#colpi dei cattivi
immagine_colpo_cattivi = pygame.image.load("immagini-gioco\\colpo cattivi.png")

#colpi del boss finale
immagine_colpo_boss = pygame.image.load("immagini-gioco\\colpo_boss_finale.png")

lista_bullet = []
#ciclo fondamentale
running = True
conta_spawnboss = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            bullet_rect = pygame.Rect(eroe.posizione_eroe_x()+28, eroe.posizione_eroe_y()-28, dim_bullet_buoni_x, dim_bullet_buoni_y)
            d = Bullet(image_proiettile_buoni, bullet_rect)
            lista_bullet.append(d)
    key_pressed = pygame.key.get_pressed()
    eroe.move(key_pressed)
    for i in range(len(lista_bullet)):
        lista_bullet[i].muovi_bullet()
    cattivi.update()
    # Controlla le collisioni tra i proiettili della navicella e nemici
    for proiettile in lista_bullet:
        for nemico in cattivi.nemici:
            if proiettile.rect.colliderect(nemico):
                cattivi.nemici.remove(nemico)
                lista_bullet.remove(proiettile)
                break
    # Controlla le collisioni tra i proiettili dei nemici e la navicella
    for proiettile in cattivi.proiettili:
        if proiettile.rect.colliderect(eroe.rect):
            eroe.colpita = True
            running = False
            cattivi.proiettili.remove(proiettile)
            break





    screen.blit(sfondo, (0, 0))

    eroe.draw(screen)
    cattivi.draw(screen)
    if cattivi.nemici_sconfitti == True:
        if conta_spawnboss>(FPS*5):
            boss.update()
            boss.draw(screen)
        conta_spawnboss+= 1
    for i in range(len(lista_bullet)):
        lista_bullet[i].disegna_bullet(screen)
    # boss.draw(screen) 
    pygame.display.flip()
    clock.tick(FPS)