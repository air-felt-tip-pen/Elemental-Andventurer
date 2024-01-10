import pygame
import sys

from main import *

class Menu:
    def __init__(self):
        self.place = 'menu'


        class MyButton(pygame.sprite.Sprite):
            def __init__(self, image, coord: list, transform: tuple):
                super().__init__()
                if type(image) == str:
                    self.image = pygame.image.load(image)
                else:
                    self.image = image
                if transform[0]:
                    self.size = transform[1]
                    self.image = pygame.transform.scale(self.image, (transform[1]))
                else:
                    self.size = self.image.get_size()
                self.rect = self.image.get_rect(topleft=coord)
                self.spare_image = self.image

            def update(self, surface, mous, mous_pressed=0):
                if self.rect.collidepoint(mous):
                    self.image = pygame.transform.scale(self.image, (self.size[0] * 1.025, self.size[1] * 1.025))
                    x, y = self.rect.topleft
                    mus = int(sum(self.size) // 100)
                    surface.blit(self.image, (x - mus, y - mus + mus // 2))
                    if pygame.mouse.get_pressed()[mous_pressed]: return True
                else:
                    self.image = pygame.transform.scale(self.spare_image, self.size)
                    surface.blit(self.image, self.rect)


        class Cards(MyButton):
            def __init__(self, image, coord:list, text: str):
                self.image = pygame.image.load('for_game//image//obj//crd.jpg')
                self.rect = self.image.get_rect(topleft=(coord))
                self.image2 = pygame.image.load(image)
                self.image2 = pygame.transform.scale(self.image2, (1920/4, 1080/4))
                self.image.blit(self.image2, (20, 280))
                self.font = pygame.font.SysFont(None, 100)
                self.text = self.font.render(text, True, (255, 255, 255))
                self.image.blit(self.text, (20, 100))
                if text.split(' ')[1] != '1':
                    self.image.blit(pygame.image.load('for_game//image//obj//lock.png'), (400, 10))
                super().__init__(self.image, coord, (False, (0, 0)))


            def update(self, surface, mous, mous_pressed=0):
                return super().update(surface, mous, mous_pressed)


        self._fon = {
            'menu': pygame.transform.scale(pygame.image.load('for_game//image//fon//menu.png'), (1920, 1080)),
            'shop': pygame.transform.scale(pygame.image.load('for_game//image//fon//fon_shop.png'), (1920, 1080)),
            'select_lvl': pygame.transform.scale(pygame.image.load('for_game//image//fon//seleckt_lvl.png'), (1920, 1080))
        }
        self._btn = {
            'menu': {
                'start': MyButton('for_game//image//btn//start.png', [600, 280], (True, (700, 149))),
                'shop': MyButton('for_game//image//btn//shop.png', [600, 280 + 230], (True, (700, 149))),
                'exit': MyButton('for_game//image//btn//exit.png', [600, 280 + 230 * 2], (True, (700, 149)))
            },
            'shop': {
                'back':
                    MyButton('for_game//image//btn//back.png', [15, 10], (True, (100, 50)))
            },
            'select_lvl': {
                'back': MyButton('for_game//image//btn//back.png', [15, 10], (True, (100, 50))),
                'left': MyButton('for_game//image//btn//stick.png', [0, 500], (True, (100, 50))),
                'right': MyButton('for_game//image//btn//stick_r.png', [1825, 500], (True, (100, 50)))
            }
        }

        self._btn_sl = {}
        for i in range(1, 7):
            self._btn['select_lvl'][str(i)] = None
            self._btn_sl[str(i)] = Cards(f'for_game//image/lvl/Lvl_{1}.jpg', [85+ (( 85*0 if int(i) in (1, 4) else 85 if int(i) in (2, 5) else 85*2)+525*(i - 1 if not int(i) >= 4 else i - 4)), 220], f'Level {i}')

        self._right_page = 1

    def update(self, surface, mous, mous_pressed=0):
        surface.blit(self._fon[self.place], (0, 0))
        for i in self._btn[self.place]:
            if self.place != 'select_lvl':
                if self._btn[self.place][i].update(surface, mous, mous_pressed): return eval(f'self._{i}_{self.place}()' if not i.isdigit() else f"self._lvl({i})")
            else:
                if i in ('back', 'left', 'right'):
                    if self._btn[self.place][i].update(surface, mous, mous_pressed): return eval(f'self._{i}_{self.place}()')
                if i.isdigit():
                    if self._right_page == 1 and not int(i) >=4:
                        if self._btn_sl[i].update(surface, mous, mous_pressed): return eval(f"self._lvl({i})")
                    elif self._right_page == 2 and not int(i) <= 3:
                        if self._btn_sl[i].update(surface, mous, mous_pressed): return eval(f"self._lvl({i})")


    # Функціонал():
    def _left_select_lvl(self):
        if self._right_page == 2:
            self._right_page -=1
            time.sleep(0.15)

    def _right_select_lvl(self):
        if self._right_page == 1:
            self._right_page +=1
            time.sleep(0.15)

    def _back_shop(self):
        self.__move('menu')

    def _lvl(self, x):
        if x == 1:
            self.__move(str(x))
            kay = False

    def _back_select_lvl(self):
        self.__move('menu')

    def _start_menu(self):
        self.__move('select_lvl')

    def _shop_menu(self):
        # self.__move('shop')
        ...

    def _exit_menu(self):
        pygame.quit()
        sys.exit()

    def __move(self, where: str):
        time.sleep(0.15)
        self.place = where
