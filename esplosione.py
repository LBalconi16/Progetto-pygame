import pygame

class Esplosione:
    def __init__(self, x, y):
        self.images = [pygame.image.load(f"immagini-gioco\\esplosione_{i}.webp") for i in range(1, 6)]  # Carica le immagini dell'esplosione
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.animation_speed = 5

    def update(self):
        self.counter += 1
        if self.counter >= self.animation_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
    
