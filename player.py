import pygame as pg
import math 

arrow = pg.image.load('ARROW.png')
arrow = pg.transform.scale(arrow, (20, 20))
arrow = pg.transform.rotate(arrow, -90)

from settings import *
from mappy import Map

centre = (WIN_WIDTH // 2, WIN_HEIGHT // 2)

class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        x = WIN_WIDTH // 2
        y = WIN_HEIGHT // 2
        self.angle = angle
        self.brrbrr = 0.02
        self.radius = 5
        self.speed = 0.5
        self.mouse_sens = 0.003

    def movement(self):
        keys = pg.key.get_pressed()

        self.prev_x = self.x
        self.prev_y = self.y
        mx, my = pg.mouse.get_rel()
        rot_delta = mx * self.mouse_sens

        forward = 0.0
        strafe = 0.0

        if keys[pg.K_w]:
            forward += self.speed
        if keys[pg.K_s]:
            forward -= self.speed
        if keys[pg.K_d]:
            strafe += self.speed
        if keys[pg.K_a]:
            strafe -= self.speed
        if keys[pg.K_r]:
            self.x = WIN_WIDTH // 2
            self.y = WIN_HEIGHT // 2
        if keys[pg.K_ESCAPE]:
            pg.quit()
            exit()

        self.angle += rot_delta

        self.x += math.cos(self.angle) * forward
        self.y += math.sin(self.angle) * forward
        perp = self.angle + math.pi/2
        self.x += math.cos(perp) * strafe
        self.y += math.sin(perp) * strafe
        
    def render(self, screen):
       screen.blit(pg.transform.rotate(arrow, -math.degrees(self.angle)), (int(self.x) - 10, int(self.y) - 10))
    
    def collision(self, x, y):
        map = Map()
        grid_x, grid_y = map.coords(x, y)
        if map.grid[grid_y][grid_x] == 1:
            self.x,self.y = (self.prev_x, self.prev_y) 
                
