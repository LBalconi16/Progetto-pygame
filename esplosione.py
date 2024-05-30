import pygame

class Esplosione:
    def __init__(self, x, y, larghezza=50, altezza=50):
        self.images = [pygame.image.load(f"immagini-gioco\\esplosione_{i}.png") for i in range(1, 6)]
        self.images = [pygame.transform.scale(img, (larghezza, altezza)) for img in self.images]  # Ridimensiona le immagini
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.counter = 0
        self.animation_speed = 5

    def update(self):
        self.counter += 1
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.index += 1
            if self.index < len(self.images):
                self.image = self.images[self.index]

    def draw(self, screen):
        if self.index < len(self.images):
            screen.blit(self.image, self.rect.topleft)
    
