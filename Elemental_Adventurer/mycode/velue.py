import pygame
import os

from mycode.Player import Player, DashPlayer, FireballPlayer, EvolvingPlayer, AllPlayer
from mycode.Floor import Box, Floor, LavaBox, WaterBox
from mycode.Enemy import Enemy
from mycode.buff import Buff
pygame.init()

# Екран
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((255, 255, 255))

clock = pygame.time.Clock()


# Рівень
lvl = pygame.Surface((3000, 1080))
lvl.fill((210, 0, 210))
lvl.set_colorkey((210, 0, 210))

current_level = 1






# Гравець
player = AllPlayer(100, 700)



coins = 0

stars = {
    'all':0,
    'lvl':0
}



# Блоки
boxes = pygame.sprite.Group()
lava_boxes = pygame.sprite.Group()
water_boxes = pygame.sprite.Group()


boxes.add(Floor())
boxes.add(Box(425+22, 987+21))
boxes.add(Box(520+22, 855+24))
boxes.add(Box(568+185, 712+161, is_=True, lala=[365, 320]))
boxes.add(Box(1015+22, 598+24))
boxes.add(Box(1177+22, 582+22))
boxes.add(Box(1319+23, 602+23))
boxes.add(Box(1458+23, 703+23))
boxes.add(Box(923+23, 494+22))
boxes.add(Box(807+23, 401+22))
boxes.add(Box(704+23, 344+24))

lava_boxes.add(LavaBox(477+23, 500+23))
water_boxes.add(WaterBox(1573, 868))





# boxes.add(Box(1015+22, 598+24, r"box_.png"))



# lava_boxes.add(LavaBox(700+300, 200+440))
# water_boxes.add(WaterBox(700+300+200, 200+440))

#
#(933, 1032)
#(365, 320)
# Противник
enemys = pygame.sprite.Group()

# enemys.add(Enemy(1500, 500, 1500, 900, 100))
# enemys.add(Enemy(1000, 1000-102, 1800, 1000-102, 100))


# Бафи
buffs = pygame.sprite.Group()
buffs.add(Buff('h', [1700, 900]))
buffs.add(Buff('h', [200, 700]))
buffs.add(Buff('h', [1250, 350]))

buffs.add(Buff('c', [1700, 900]))
buffs.add(Buff('c', [200, 700]))
buffs.add(Buff('c', [1250, 350]))

buffs.add(Buff('s', [1700, 900]))
buffs.add(Buff('s', [200, 700]))
buffs.add(Buff('s', [1250, 350]))