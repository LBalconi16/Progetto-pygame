import pygame
import time

WIDTH, HEIGHT = 800, 600
VEL = 5

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load('missili dei buoni.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def shoot(self):
        current_time = time.time()

        # 1 secondo tra i proiettili
        if current_time - self.last_shot_time >= 1:  
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.append(bullet)
            self.last_shot_time = current_time


    def update(self):
        for bullet in self.bullets:
            bullet.update()
            # Rimuove i proiettili che escono dallo schermo
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)