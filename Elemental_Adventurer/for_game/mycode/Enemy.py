import pygame
import os
pygame.init()
class Enemy(pygame.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2, hp):
        super().__init__()

        current_path = os.path.abspath(os.getcwd())
        new_path = r"for_game//image//obj"
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
        self.speed = 3

        self.direction = -1

    def update(self, player):
        self.move()
        if self.rect.colliderect(player.attack.image.get_rect(topleft=(player.attack.rect.x, player.attack.rect.y))) and player.attack_visible  :
            self.hp -= 10

        for attacket in player.projectiles:
            if self.rect.colliderect(attacket.rect) :
                self.hp -= 2.5

        if self.hp <= 0:
            self.kill()



    def move(self): # Рухайте противника в напрямку цілі.

        direction = (self.target_x - self.rect.x, self.target_y - self.rect.y)
        delta = (min(self.speed, abs(direction[0])), min(self.speed, abs(direction[1])))
        if direction[0] < 0:
            delta = (-delta[0], delta[1])
        elif direction[1] < 0:
            delta = (delta[0], -delta[1])
        self.rect.x += delta[0]
        self.rect.y += delta[1]

        if self.start_pos < self.end_pos:
            if (self.rect.x, self.rect.y) >= self.end_pos:
                self.target_x, self.target_y = self.start_pos
        elif (self.rect.x, self.rect.y) <= self.start_pos:
            self.target_x, self.target_y = self.end_pos

        if self.end_pos > self.start_pos:
            if (self.rect.x, self.rect.y) <= self.start_pos:
                self.target_x, self.target_y = self.end_pos
        elif (self.rect.x, self.rect.y) >= self.end_pos:
            self.target_x, self.target_y = self.start_pos

