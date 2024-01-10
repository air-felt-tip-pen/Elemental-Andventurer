import pygame
import os
pygame.init()
class Buff(pygame.sprite.Sprite):
    def __init__(self, type: str, coord: list):
        super().__init__()
        self.type = type
        current_path = os.path.abspath(os.getcwd())
        new_path = r"for_game//image//obj"
        os.chdir(new_path)

        self.img = 0
        self.anim = 0
        self.i = 0
        self.dir = 1

        if type == 'h':
            a = 'heart'
            self.anim = 3

        elif type == 'c':
            a = 'coin'
            self.anim = 5
        elif type == 'k':
            a = 'key'
            self.anim = 4
        else:
            a = 'credit'
            self.anim = 4

        self.images = [pygame.image.load(f"{a}//{i}.png") for i in range(self.anim)]
        self.image = self.images[0]

        self.rect = self.image.get_rect(topleft=coord)

        os.chdir(current_path)

    def update(self):
        if self.i < 7:
            self.i +=1
        else:
            if self.dir==1 and self.img==self.anim-1:
                self.dir = -1
            elif self.dir==-1 and self.img==0:
                self.dir = 1
            self.img+=self.dir
            self.i = 0
        self.image = self.images[self.img]





