import time
from mycode.velue import *
from mycode.Father_class import Lvl

pygame.init()


class Lvl1(Lvl):
    def __init__(self, screen):
        super().__init__(screen)

        # Блоки
        self.boxes = pygame.sprite.Group()
        self.lava_boxes = pygame.sprite.Group()
        self.water_boxes = pygame.sprite.Group()

        self.boxes.add(Floor())
        self.boxes.add(Box(425 + 22, 987 + 21))
        self.boxes.add(Box(520 + 22, 855 + 24))
        self.boxes.add(Box(568 + 185, 712 + 161, is_=True, lala=[365, 320]))
        self.boxes.add(Box(1015 + 22, 598 + 24))
        self.boxes.add(Box(1177 + 22, 582 + 22))
        self.boxes.add(Box(1319 + 23, 602 + 23))
        self.boxes.add(Box(1458 + 23, 703 + 23))
        self.boxes.add(Box(923 + 23, 494 + 22))
        self.boxes.add(Box(807 + 23, 401 + 22))
        self.boxes.add(Box(704 + 23, 344 + 24))

        self.lava_boxes.add(LavaBox(477 + 23, 500 + 23))
        self.water_boxes.add(WaterBox(1573, 868))

        self.enemys = pygame.sprite.Group()

        # Бафи
        self.buffs = pygame.sprite.Group()
        self.buffs.add(Buff('h', [1700, 900]))
        self.buffs.add(Buff('h', [200, 700]))
        self.buffs.add(Buff('h', [1250, 350]))

        self.buffs.add(Buff('c', [1700, 900]))
        self.buffs.add(Buff('c', [200, 700]))
        self.buffs.add(Buff('c', [1250, 350]))

        self.buffs.add(Buff('s', [1700, 900]))
        self.buffs.add(Buff('s', [200, 700]))
        self.buffs.add(Buff('s', [1250, 350]))



class Game():
    def __init__(self):
        self.is_first_game = True
        self.lvl = {
            '1': Lvl1(screen)
        }

    def standart_player_in_game(self):
        global coins
        floor_group = self.lvl[self.menu.place].boxes.copy()
        if player.__str__()[1] == "A" or player.__str__()[1] == "E":
            if player.material == "water":
                for i in self.lvl[self.menu.place].water_boxes:
                    floor_group.add(i)

            if player.material == "lava":
                for i in self.lvl[self.menu.place].lava_boxes:
                    floor_group.add(i)

        self.__UpdateDraw(screen, player, floor_group)

        for i in self.lvl[self.menu.place].buffs:
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
                self.lvl[self.menu.place].buffs.remove(i)
        self.lvl[self.menu.place].buffs.draw(screen)

        self.__UpdateDraw(screen, self.lvl[self.menu.place].enemys, player)

    def update(self):
        if pygame.mouse.get_pressed()[1]:
            print(pygame.mouse.get_pos())

        if self.is_first_game:
            self.is_first_game = False
            self.__pregame()

        if self.menu.place == "menu" or self.menu.place == "shop" or self.menu.place == 'select_lvl':
            self.menu.update(screen, pygame.mouse.get_pos())

        elif self.menu.place.isdigit():

            global coins
            pygame.event.pump()

            self.lvl[self.menu.place].update()
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
            self.lvl[self.menu.place].boxes.draw(lvl)
            self.lvl[self.menu.place].lava_boxes.draw(lvl)
            self.lvl[self.menu.place].water_boxes.draw(lvl)



            screen.blit(lvl, (0, 0), (0, 0, lvl.get_width(), lvl.get_height()))

    def __UpdateDraw(self, surface, obj, *args):
        obj.update(*args)
        obj.draw(surface)

    def __pregame(self):
        from mycode.menu import Menu
        self.menu = Menu()


game = Game()

