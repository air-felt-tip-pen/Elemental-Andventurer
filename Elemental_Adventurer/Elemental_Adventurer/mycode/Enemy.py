import pygame
import os
pygame.init()
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2, hp):
        super().__init__()

        current_path = os.path.abspath(os.getcwd())
        new_path = r"image"
        os.chdir(new_path)
        # Завантажте зображення противника.
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        os.chdir(current_path)

        self.hp = hp

        self.start_pos = (x1, y1)
        self.end_pos = (x2, y2)

        # Встановіть початкову позицію противника.
        self.rect.x = x1
        self.rect.y = y1

        # Встановіть координати цілі та швидкість руху.
        self.target_x = x2
        self.target_y = y2
        self.speed = 2

        self.direction = -1

    def update(self, player):
        self.move()
        if self.rect.colliderect(player.attack.image.get_rect(topleft=(player.attack.rect.x, player.attack.rect.y))) and player.attack_visible  :
            self.hp -= 25

        for attacket in player.projectiles:
            if self.rect.colliderect(attacket.rect) :
                self.hp -= 100

        if self.hp <= 0:
            self.kill()



    def move(self): # Рухайте противника в напрямку цілі.

        if self.rect.x < self.target_x:
            self.rect.x += self.speed
        elif self.rect.x > self.target_x:
            self.rect.x -= self.speed

        if self.rect.y < self.target_y:
            self.rect.y += self.speed
        elif self.rect.y > self.target_y:
            self.rect.y -= self.speed

        if self.start_pos < self.end_pos:

            if self.end_pos <= (self.rect.x, self.rect.y):
                self.target_x = self.start_pos[0]
                self.target_y = self.start_pos[1]

            if self.start_pos >= (self.rect.x, self.rect.y):
                self.target_x = self.end_pos[0]
                self.target_y = self.end_pos[1]

        else:

            if self.end_pos >= (self.rect.x, self.rect.y):
                self.target_x = self.start_pos[0]
                self.target_y = self.start_pos[1]

            if self.start_pos <= (self.rect.x, self.rect.y):
                self.target_x = self.end_pos[0]
                self.target_y = self.end_pos[1]
