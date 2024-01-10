import pygame
import os

from for_game.mycode.Player import Player, DashPlayer, FireballPlayer, EvolvingPlayer, AllPlayer
from for_game.mycode.Floor import Box, Floor, LavaBox, WaterBox
from for_game.mycode.Enemy import Enemy
from for_game.mycode.buff import Buff
from for_game.mycode.Father_class import WindowWin
pygame.init()

# Екран
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
screen.fill((255, 255, 255))

clock = pygame.time.Clock()


# Рівень
lvl = pygame.Surface((3000, 1080))
lvl.fill((210, 0, 210))
lvl.set_colorkey((210, 0, 210))

current_level = 1






# Гравець
player = AllPlayer(100, 700)


kay = False


coins = {
    'current': 0,
    'total': 0,
    'lvl': {
        1:1,
        2:1,
        3:1,
        4:1,
        5:1,
        6:1
    }
}



win = WindowWin([400, 300])
win.image = pygame.image.load(r"for_game/image/fon/win.jpg")

is_win = False
