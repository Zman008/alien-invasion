import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, 1, 10)

    def update(self):
        self.rect.y += 4
        self.rect.x += 1

    def draw_rain(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
