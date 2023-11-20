import pygame
import os
from mycode.Father_class import Sprite
import numpy
import time
pygame.init()

class Player(Sprite):
    def __init__(self, start_x, start_y):
        current_path = os.path.abspath(os.getcwd())
        super().__init__("image//player//Idle//1.png", start_x, start_y)
        self.all_image = {
            "run" : [pygame.image.load(f'image//player//Run//{i}.png') for i in range(1, 7)],
            "idle" : [pygame.image.load(f'image//player//Idle//{i}.png') for i in range(1, 5)]
        }
        self.anim_sleep = 0
        self.anim = 'idle'
        self.animation_index = 0
        self.facing_left = False


        self.image = self.all_image["idle"][0]
        self.rect = self.image.get_rect(topleft=(start_x, start_y))
        self.rect.w += 20


        self.start_x, self.start_y = start_x, start_y
        self.stand_image = self.image

        self.projectiles = pygame.sprite.Group()

        self.health = 100
        # self.immortality = 200

        # Рух
        self.walk_speed = 4
        self.run_speed = 8
        self.speed = self.walk_speed
        self.jump_speed = 25
        self.vsp = 0
        self.gravity = 1.5
        self.min_jump_speed = 4
        self.prev_key = pygame.key.get_pressed()
        self.direction = "right" # Початковий напрямок персонажа.

        self.double_press_timer = 0
        self.double_press_delay = 0.1  # Задайте затримку для визначення подвійного натискання (у секундах).
        self.is_running = False  # Додайте змінну для відстеження, чи перебуває персонаж у режимі бігу.

        # Атака
        # Встановіть навички персонажа.
        self.attack = pygame.sprite.Sprite()
        self.attack.image = pygame.image.load("image//attack.png")
        self.attack.rect = self.attack.image.get_rect()
        self.attack.rect.centerx = self.rect.centerx
        self.attack.rect.centery = self.rect.centery
        self.attack_visible = False

        # Змінні для кулдауна атаки
        self.attack_cooldown = 0.5  # Кулдаун атаки в секундах
        self.last_attack_time = 0

        os.chdir(current_path)

    def update(self, boxes):
        if self.rect.y > 1050:
            self.rect.x = self.start_x
            self.rect.y = self.start_y

        hsp = 0
        ong_round = self.check_collision(0, 1, boxes)
        # check keys
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect.x > 0:
            self.direction = "left"
            self.facing_left = True
            hsp = -self.speed

            # Перевірка для подвійного натискання "A"
            if self.prev_key[
                pygame.K_a] and pygame.time.get_ticks() - self.double_press_timer < self.double_press_delay * 1000:
                self.is_running = not self.is_running  # Змінити стан бігу
            else:
                self.double_press_timer = pygame.time.get_ticks()
        elif key[pygame.K_d] and self.rect.x < 1920-self.rect.h:
            self.direction = "right"
            self.facing_left = False
            hsp = self.speed

            # Перевірка для подвійного натискання "A"
            if self.prev_key[
                pygame.K_d] and pygame.time.get_ticks() - self.double_press_timer < self.double_press_delay * 1000:
                self.is_running = not self.is_running  # Змінити стан бігу
            else:
                self.double_press_timer = pygame.time.get_ticks()
        else:
            self.image = self.stand_image

            # Оновлення швидкості відповідно до стану бігу/ходьби
            if self.is_running:
                self.speed = self.run_speed
            else:
                self.speed = self.walk_speed
                self.image = self.stand_image

        # Перевірка стику з ворогами
        from mycode.funk import game
        enemys = game.lvl[game.menu.place].enemys
        if enemys:
            enemy_collision = pygame.sprite.spritecollide(self, enemys, False)
            enemy_x = 1000
            for enemy in enemy_collision:
                enemy_x = enemy.rect.x  # X координата спрайту enemy
            if enemy_collision:
                self.vsp = -self.jump_speed // 2.5
                if self.rect.x < enemy_x:
                    hsp += -20*2
                else:
                    hsp += 20*2
                self.health -= 10  # Зменшення здоров'я на 20

        if key[pygame.K_w] and ong_round:
            self.vsp = -self.jump_speed

        # variable height jumping
        if self.prev_key[pygame.K_w] and not key[pygame.K_w]:
            if self.vsp < -self.min_jump_speed:
                self.vsp = -self.min_jump_speed

                # Встановлення видимості атаки та позиції атаки.
        current_time = time.time()
        if pygame.mouse.get_pressed()[0] and (current_time - self.last_attack_time) >= self.attack_cooldown:
            self.attack.rect.x = self.rect.x - 30 if self.direction == "left" else self.rect.x + 100
            self.attack.rect.y = self.rect.y
            self.attack_visible = True
            self.last_attack_time = current_time
        else:
            self.attack_visible = False

        self.prev_key = key

        # gravity
        if self.vsp < 10 and not ong_round:  # 9.8 rounded up
            self.vsp += self.gravity

        if ong_round and self.vsp > 0:
            self.vsp = 0

        # movement
        self.move(hsp, self.vsp, boxes)

    def move(self, x, y, boxes):
        dx = x
        dy = y

        while self.check_collision(0, dy, boxes):
            dy -= numpy.sign(dy)


        while self.check_collision(dx, dy, boxes):
            dx -= numpy.sign(dx)

        self.rect.move_ip([dx, dy])

    def check_collision(self, x, y, grounds):
        self.rect.move_ip([x, y])
        collide = pygame.sprite.spritecollideany(self, grounds)
        self.rect.move_ip([-x, -y])
        return collide

    def draw(self, screen):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] or key[pygame.K_d]:
            self.anim = 'run'
        else:
            self.anim = 'idle'

        a = 6 if self.anim == 'run' else 4
        if self.anim_sleep < 6:
            self.anim_sleep += 1
        else:
            self.anim_sleep = 0
            if self.animation_index < a-1:
                self.animation_index += 1
                self.image = self.all_image[self.anim][self.animation_index]
            else:
                self.animation_index = 0



        # Відображення персонажа на екрані залежно від напрямку.
        if self.direction == "right":
            screen.blit(self.image, self.rect)
        else:
            flipped_image = pygame.transform.flip(self.image, True, False)
            screen.blit(flipped_image, self.rect)

        # Відображення атаки на екрані залежно від стану атаки.
        if self.attack_visible:
            if self.direction == "right":
                screen.blit(self.attack.image, (self.attack.rect.x-15, self.attack.rect.y))
            else:
                flipped_image_attack = pygame.transform.flip(self.attack.image, True, False)
                screen.blit(flipped_image_attack, (self.attack.rect.x-18, self.attack.rect.y))

class DashPlayer(Player):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.dash_speed = 40
        self.dash_duration = 0.2
        self.dash_cooldown = 2.0
        self.last_dash_time = 0
        self.dashing = False
        self.dash_start_time = 0
        self.dash_direction = "right"

    def update(self, boxes):
        current_time = time.time()
        if current_time - self.last_dash_time >= self.dash_cooldown:
            if pygame.key.get_pressed()[pygame.K_SPACE] and not self.dashing:
                self.dash()

        if self.dashing:
            self.handle_dash(current_time, boxes)
        else:
            super().update(boxes)

    def dash(self):
        self.dashing = True
        self.dash_start_time = time.time()
        self.dash_direction = "right" if not self.facing_left else "left"

    def handle_dash(self, current_time, boxes):
        elapsed_time = current_time - self.dash_start_time


        if elapsed_time < self.dash_duration:
            if self.dash_direction == "right":
                dx = self.dash_speed
            else:
                dx = -self.dash_speed

            self.move(dx, 0, boxes)
        else:
            self.dashing = False
            self.last_dash_time = current_time

class FireballPlayer(Player):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)

        # Змінні для дальньої атаки
        self.projectile_speed = 10
        self.projectile_cooldown = 3.0  # Кулдаун дальньої атаки в секундах
        self.last_projectile_time = 0

    def update(self, boxes):
        super().update(boxes)
        current_time = time.time()

        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[2] and (current_time - self.last_projectile_time) >= self.projectile_cooldown:
            mouse_pos = pygame.mouse.get_pos()
            projectile = pygame.sprite.Sprite()
            current_path = os.path.abspath(os.getcwd())
            new_path = r"image"
            os.chdir(new_path)
            projectile.image = pygame.image.load("fireball.png")
            os.chdir(current_path)
            projectile.rect = projectile.image.get_rect()
            projectile.rect.centerx = self.rect.centerx
            projectile.rect.centery = self.rect.centery
            if self.direction == "right":
                projectile.direction = "right"
            else:
                projectile.direction = "left"
            self.projectiles.add(projectile)
            self.last_projectile_time = current_time

        # Рух дальних атак
        for projectile in self.projectiles:
            if projectile.direction == "right":
                projectile.rect.x += self.projectile_speed
            else:
                projectile.rect.x -= self.projectile_speed

            # Перевірка зіткнення з підлогою
            if pygame.sprite.spritecollideany(projectile, boxes):
                self.projectiles.remove(projectile)




            if projectile.rect.x >= 1920 or projectile.rect.x < 0:
                self.projectiles.remove(projectile)

    def draw(self, screen):
        super().draw(screen)
        self.projectiles.draw(screen)

class EvolvingPlayer(Player):
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        self.material_cooldown = 0.5  # Кулдаун для зміни матерії в секундах
        self.last_material_change_time = 0
        self.material = "lava"

    def update(self, boxes):
        super().update(boxes)

        key = pygame.key.get_pressed()
        current_time = time.time()

        from mycode.funk import game
        lava_boxes, water_boxes = game.lvl[game.menu.place].lava_boxes, game.lvl[game.menu.place].water_boxes

        if lava_boxes or water_boxes:
            if self.material == "water":
                aaa = pygame.sprite.spritecollide(self, lava_boxes, False)
            else:
                aaa = pygame.sprite.spritecollide(self, water_boxes, False)
            if not aaa:
                if key[pygame.K_e] and (current_time - self.last_material_change_time) >= self.material_cooldown:
                    self.last_material_change_time = current_time
                    if self.material == "lava":
                        self.material = "water"
                    else:
                        self.material = "lava"

class AllPlayer(DashPlayer, FireballPlayer, EvolvingPlayer):
    def __init__(self, player_x, player_y):
        super().__init__(player_x, player_y)
