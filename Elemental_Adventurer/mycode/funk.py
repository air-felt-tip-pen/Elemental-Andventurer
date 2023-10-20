import time
from mycode.velue import *

pygame.init()

class Lvl1():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('image/lvl/lvl_1.jpg'), (1920, 1080))



    def update(self):
        screen.blit(self.image, (0, 0))

class Game():
    def __init__(self):
        self.is_first_game = True

    def standart_player_in_game(self):
        global coins
        floor_group = boxes.copy()
        if player.__str__()[1] == "A" or player.__str__()[1] == "E":
            if player.material == "water":
                for i in water_boxes:
                    floor_group.add(i)

            if player.material == "lava":
                for i in lava_boxes:
                    floor_group.add(i)

        self.__UpdateDraw(screen, player, floor_group)

        for i in buffs:
            if player.rect.colliderect(i.rect):
                if i.type == 'h':
                    if player.health + 25 > 100:
                        player.health = 100
                    else:
                        player.health += 25
                elif i.type == 'c':
                    coins += 1
                else:
                    stars["lvl"] += 1
                buffs.remove(i)
        buffs.draw(screen)

        self.__UpdateDraw(screen, enemys, player)

    def update(self):
        if pygame.mouse.get_pressed()[1]:
            print(pygame.mouse.get_pos())

        if self.is_first_game:
            self.is_first_game = False
            self.__pregame()

        place = self.menu.place
        if place == "menu" or place == "shop" or place == "select_lvl":
            self.menu.update(screen, pygame.mouse.get_pos())
        else:

            global coins
            pygame.event.pump()

            Lvl1().update()
            self.standart_player_in_game()


            font = pygame.font.Font(None, 36)
            health_text = font.render(f"Health: {player.health}", True, (255, 255, 255))
            coins_text = font.render(f"Coins: {coins}", True, (255, 255, 255))
            stars_text = font.render(f"Stars: {stars['lvl']}", True, (255, 255, 255))
            material_text = font.render(f"Material: {player.material}", True, (255, 255, 255))
            screen.blit(health_text, (10, 10))
            screen.blit(coins_text, (10, 10 + 35))
            screen.blit(stars_text, (10, 10 + 35 + 35))
            screen.blit(material_text, (10, 10 + 35 + 35 + 35))
            boxes.draw(lvl)
            lava_boxes.draw(lvl)
            water_boxes.draw(lvl)



            screen.blit(lvl, (0, 0), (0, 0, lvl.get_width(), lvl.get_height()))

    def __UpdateDraw(self, surface, obj, *args):
        obj.update(*args)
        obj.draw(surface)

    def __pregame(self):
        from mycode.menu import Menu
        self.menu = Menu()


game = Game()

