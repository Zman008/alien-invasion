import pygame

class Mouth:
    def __init__(self, ai_o):
        self.screen = ai_o.screen
        self.screen_rect = ai_o.screen.get_rect()
        self.image = pygame.image.load('images/mouth.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + 50
    def blitme(self):
        self.screen.blit(self.image, self.rect)