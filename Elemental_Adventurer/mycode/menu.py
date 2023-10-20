from main import *


class Menu:
    def __init__(self):

        class MyButton(pygame.sprite.Sprite):
            def __init__(self, image, coord: list, transform: tuple):
                super().__init__()
                self.image = pygame.image.load(image)
                if transform[0]:
                    self.size = transform[1]
                    self.image = pygame.transform.scale(self.image, (transform[1]))
                else: self.size = self.image.get_size()
                self.rect = self.image.get_rect(topleft=coord)
                self.spare_image = self.image

            def update(self, surface, mous, mous_pressed=0):

                if self.rect.collidepoint(mous):
                    self.image = pygame.transform.scale(self.image, (self.size[0] * 1.025, self.size[1] * 1.025))
                    x, y, *a = self.rect
                    del a
                    mus = int(self.size[0] + self.size[1]) // 100
                    surface.blit(self.image, (x - mus, y - mus+mus//2))
                    if pygame.mouse.get_pressed()[mous_pressed]:
                        return True
                else:
                    self.image = pygame.transform.scale(self.spare_image, self.size)
                    surface.blit(self.image, self.rect)

        self.place = 'menu'


        self._fon_menu = pygame.transform.scale(pygame.image.load('menu.png'), (1920, 1080))
        self._btn_menu = {
            'start': MyButton('start.png', [600, 280], (True, (700, 149))),
            'shop': MyButton('shop.png', [600, 280 + 230], (True, (700, 149))),
            'exit': MyButton('exit.png', [600, 280 + 230 * 2], (True, (700, 149)))
        }

        self._fon_shop = pygame.transform.scale(pygame.image.load('fon_shop.png'), (1920, 1080))
        self._btn_shop = {
            'back': MyButton('back.png', [15, 10], (True, (100, 50)))
        }


    def update(self, surface, mous, mous_pressed=0):
        if self.place == 'menu':
            surface.blit(self._fon_menu, (0, 0))
            for i in self._btn_menu:
                if self._btn_menu[i].update(surface, mous):
                    eval(f'self._{i}_{self.place}()')
        elif self.place == 'shop':
            surface.blit(self._fon_shop, (0, 0))
            for i in self._btn_shop:
                if self._btn_shop[i].update(surface, mous):
                    eval(f'self._{i}_{self.place}()')

    def _back_shop(self):
        time.sleep(0.15)
        self.place = 'menu'

    def _start_menu(self):
        time.sleep(0.15)
        self.place = 'lvl1'

    def _shop_menu(self):
        time.sleep(0.15)
        self.place = 'shop'

    def _exit_menu(self):
        pygame.quit()
        exit()







