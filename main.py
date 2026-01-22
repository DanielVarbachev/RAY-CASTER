import pygame as pg
from settings import *
from mappy import *
from player import Player
from raycaster import Raycaster
from ghost_1 import Ghost_1

clock = pg.time.Clock()

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pg.mouse.set_visible(False)
pg.event.set_grab(True)
pg.mouse.get_rel()

map = Map()
ghost = Ghost_1(14 * TS, 3 * TS)
player = Player(WIN_WIDTH // 2, WIN_HEIGHT // 2, 0)

raycaster = Raycaster(player, map)

while True:
    clock.tick(240)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill((150, 75, 0))

    map.render(screen)
    player.render(screen)
    if brrbrr >= 1:
        ghost.movement()
        brrbrr = 0
    ghost.render(screen)
    player.collision(player.x, player.y)
    player.movement()
    raycaster.castAllRays(screen)
    #raycaster.render(screen)

    brrbrr += 1/240

    pg.display.update()