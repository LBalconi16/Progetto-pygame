import pygame
import random 
import time
from eroe import Eroe
from cattivi import Cattivi
from boss import Boss
from sparo import Bullet
from esplosione import Esplosione

WIDTH, HEIGHT = 800, 600

# Inizializzazione di Pygame
pygame.init()

# Finestra base
clock = pygame.time.Clock()
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Gioco navicelle')

# Caricamento delle immagini
sfondo = pygame.image.load("immagini-gioco\\sfondo1.jpg")
sfondo  = pygame.transform.scale(sfondo, (WIDTH, HEIGHT))
sfondo_win = pygame.image.load('immagini-gioco\\win.png')
sfondo_win = pygame.transform.scale(sfondo_win, (WIDTH, HEIGHT))
sfondo_lose = pygame.image.load('immagini-gioco\\game_over.png')
sfondo_lose  = pygame.transform.scale(sfondo_lose, (WIDTH, HEIGHT))

# Creazione degli oggetti di gioco
eroe = Eroe()
cattivi = Cattivi(3, 12)
boss = Boss()
FPS = 60
# vita eroe e boss
vita_eroe = 5
vita_boss = 100

win = True
lose = True

# Dimensioni proiettili
dim_bullet_buoni_x = 35
dim_bullet_buoni_y = 50
dim_bullet_cattivi_x = 35
dim_bullet_cattivi_y = 50

# Caricamento immagini boss e proiettili
immagine_boss = pygame.image.load("immagini-gioco\\nave boss.webp")
immagine_boss1 = pygame.image.load("immagini-gioco\\nave_boss1.png")
immagine_boss2 = pygame.image.load("immagini-gioco\\nave_boss2.png")
immagine_colpo_buoni = pygame.image.load("immagini-gioco\\colpo buoni.png.png")
image_proiettile_buoni = pygame.transform.rotate(immagine_colpo_buoni, 90)
immagine_colpo_cattivi = pygame.image.load("immagini-gioco\\colpo cattivi.png")
immagine_colpo_boss = pygame.image.load("immagini-gioco\\colpo_del_boss.png")

lista_bullet = []
esplosioni = []

# Ciclo fondamentale
running = True
conta_spawnboss = 0
conta_vittoria = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # lista proiettili
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            bullet_rect = pygame.Rect(eroe.posizione_eroe_x() + 37, eroe.posizione_eroe_y() - 31, dim_bullet_buoni_x, dim_bullet_buoni_y)
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
                esplosioni.append(Esplosione(nemico.centerx, nemico.centery))
                cattivi.nemici.remove(nemico)
                lista_bullet.remove(proiettile)
                break

    # Controlla le collisioni tra i proiettili dei nemici e la navicella
    for proiettile in cattivi.proiettili:
        if proiettile.rect.colliderect(eroe.rect):
            vita_eroe -= 1
            if vita_eroe == 0:
                lose = False
                esplosioni.append(Esplosione(eroe.rect.centerx, eroe.rect.centery, 120, 120))
            esplosioni.append(Esplosione(eroe.rect.centerx, eroe.rect.centery, 80, 80))
            cattivi.proiettili.remove(proiettile)
            break

    screen.blit(sfondo, (0, 0))

    eroe.draw(screen)
    cattivi.draw(screen)

    if cattivi.nemici_sconfitti and vita_boss >= 0:
        if conta_spawnboss > (FPS * 5):
            if vita_boss >= 67:
                boss.draw(screen, immagine_boss, vita_boss)
            elif vita_boss >= 34:
                boss.draw(screen, immagine_boss1, vita_boss)
            else:
                boss.draw(screen, immagine_boss2, vita_boss)
            boss.update(vita_boss)
            
            # Controlla le collisioni tra i proiettili del boss e la navicella
            for proiettile in boss.proiettili:
                if proiettile.rect.colliderect(eroe.rect):
                    vita_eroe -= 1
                    if vita_eroe == 0:
                        esplosioni.append(Esplosione(eroe.rect.centerx, eroe.rect.centery, 120, 120))
                        lose = False
                    esplosioni.append(Esplosione(eroe.rect.centerx, eroe.rect.centery, 80, 80))
                    boss.proiettili.remove(proiettile)
                    break
            
            # Controlla le collisioni tra i proiettili della navicella e boss
            for proiettile in lista_bullet:
                if vita_boss >= 67:
                    if vita_boss == 67:
                        if proiettile.rect.colliderect(boss.figura_colpita1a) or proiettile.rect.colliderect(boss.figura_colpita2a):
                            esplosioni.append(Esplosione(200, 200, 350, 350))
                            vita_boss -= 1
                            lista_bullet.remove(proiettile)
                            break
                    else:
                        if proiettile.rect.colliderect(boss.figura_colpita1a) or proiettile.rect.colliderect(boss.figura_colpita2a):
                            vita_boss -= 1
                            lista_bullet.remove(proiettile)
                            break
                elif vita_boss >= 34:
                    if vita_boss == 34:
                        if proiettile.rect.colliderect(boss.figura_colpita1a) or proiettile.rect.colliderect(boss.figura_colpita2a):
                            esplosioni.append(Esplosione(600, 200, 350, 350))
                            vita_boss -= 1
                            lista_bullet.remove(proiettile)
                            break
                    else:
                        if proiettile.rect.colliderect(boss.figura_colpita1b) or proiettile.rect.colliderect(boss.figura_colpita2b):
                            vita_boss -= 1
                            lista_bullet.remove(proiettile)
                            break
                elif vita_boss>=1:
                    if proiettile.rect.colliderect(boss.figura_colpita1c) or proiettile.rect.colliderect(boss.figura_colpita2c):
                        vita_boss -= 1
                        lista_bullet.remove(proiettile)
                        break
                else:
                    if vita_boss == 0:
                        win = False
                        esplosioni.append(Esplosione(WIDTH/2, HEIGHT/2, 350, 350))
                        vita_boss -= 1
            
            # Controlla le collisioni tra la navicella e il boss
            if vita_boss >= 67:
                if eroe.rect.colliderect(boss.figura_colpita1a) or eroe.rect.colliderect(boss.figura_colpita2a):
                    lose = False    
            elif vita_boss >= 34:
                if eroe.rect.colliderect(boss.figura_colpita1b) or eroe.rect.colliderect(boss.figura_colpita2b):
                    lose = False
            else:
                if eroe.rect.colliderect(boss.figura_colpita1c) or eroe.rect.colliderect(boss.figura_colpita2c):
                    lose = False
                
        conta_spawnboss += 1

    # Controlla le collisioni tra la navicella e i nemici
    for nemico in cattivi.nemici:
        if eroe.rect.colliderect(nemico):
            lose = False
            break

    for i in range(len(lista_bullet)):
        lista_bullet[i].disegna_bullet(screen)

    # Disegna le esplosioni
    for esplosione in esplosioni:
        esplosione.update()
        esplosione.draw(screen)
    
    esplosioni = [e for e in esplosioni if e.index != len(e.images) - 1]

    if lose == False:
        screen.blit(sfondo_lose, (0, 0))
    if win == False:
        if conta_vittoria>=(FPS*2):
            screen.blit(sfondo_win, (0, 0))
        conta_vittoria+=1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()