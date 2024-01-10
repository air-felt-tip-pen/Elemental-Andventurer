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


class Lvl():

    class Portal(pygame.sprite.Sprite):
        def __init__(self):
            self.image = pygame.image.load("for_game//image//obj//portal.png")
            self.image_E = pygame.image.load("for_game//image//obj//portal_E.png")
            self.img = [self.image, self.image_E]
            self.rect = self.image.get_rect()
            self.rect.topleft = [1756, 880]
            self.num = 0




    def __init__(self, screen):
        self.image = pygame.transform.scale(pygame.image.load('for_game//image/lvl/lvl_1.jpg'), (1920, 1080))
        self.portal = self.Portal()
        self.screen = screen

    def update(self):
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.portal.img[self.portal.num], (self.portal.rect.x, self.portal.rect.y-(self.portal.num*20)))


class WindowWin(pygame.sprite.Sprite):
    def __init__(self, coord: list):
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
        self.image = pygame.Surface([1200, 500])
        self.rect = self.image.get_rect()
        self.rect.topleft = coord
        self.btn = {
            'back': MyButton("for_game/image/btn/manu.png", [50+100+coord[0], 200+coord[1]+100], (True, (280, 125))),
            'restart': MyButton("for_game/image/btn/restart.png", [350+100+coord[0], 200+coord[1]+100], (True, (280, 125))),
            'next': MyButton("for_game/image/btn/next.png", [650+100+coord[0], 200+coord[1]+100], (True, (280, 125))),
        }
        for i in self.btn:
            self.image.blit(self.btn[i].image, self.btn[i].rect)

        self.fond = pygame.font.Font(None, 200)
        self.winText = self.fond.render('You pressed', False, (150, 150, 150))
        self.winText_rect = (coord[0]+180, coord[1]+95)

    def update(self, surface, mous, mous_pressed=0):
        surface.blit(self.winText, self.winText_rect)
        for i in self.btn:
            if self.btn[i].update(surface, mous, mous_pressed):
                if i == 'back':
                    return 1
                elif i == 'restart':
                    return 2
                elif i == 'next':
                    return 3

    def draw(self, surface):
        surface.blit(self.image, self.rect)

















