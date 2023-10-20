import pygame
pygame.init()


class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, start_x, start_y, is_=False, lala=[]):
        super().__init__()
        if not is_:
            self.image = pygame.image.load(image)
        else:
            self.image = pygame.Surface(lala)
            self.image.fill((0, 0, 0))
            self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.center = [start_x, start_y]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
