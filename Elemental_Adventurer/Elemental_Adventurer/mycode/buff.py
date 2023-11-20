import pygame
import os
pygame.init()
class Buff(pygame.sprite.Sprite):
    def __init__(self, type: str, coord: list):
        super().__init__()
        self.type = type
        current_path = os.path.abspath(os.getcwd())
        new_path = r"image"
        os.chdir(new_path)

        if type == 'h': self.image = pygame.image.load('health.png')
        elif type == 'c': self.image = pygame.image.load('coin.png')
        else: self.image = pygame.image.load('star.png')

        self.rect = self.image.get_rect(topleft=coord)

        os.chdir(current_path)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
