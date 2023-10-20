import pygame.sprite
import os
from mycode.Father_class import Sprite
pygame.init()

class Box(Sprite):
    def __init__(self, start_x, start_y, image="box.png", is_=False, lala=[]):
        current_path = os.path.abspath(os.getcwd())
        os.chdir("image")
        if is_:
            super().__init__(image, start_x, start_y, is_=True, lala=lala)
        else:
            super().__init__(image, start_x, start_y)
        os.chdir(current_path)

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1920, 80))
        self.image.fill((100, 0, 210))
        self.rect = self.image.get_rect(topleft=(0, 1032))
        self.image.set_colorkey((100, 0, 210))

class LavaBox(Sprite):
    def __init__(self, start_x, start_y):
        current_path = os.path.abspath(os.getcwd())
        os.chdir("image")
        super().__init__("lava.png", start_x, start_y)
        os.chdir(current_path)

class WaterBox(Sprite):
    def __init__(self, start_x, start_y):
        current_path = os.path.abspath(os.getcwd())
        os.chdir("image")
        super().__init__("water.png", start_x, start_y)
        os.chdir(current_path)
