import pygame as pg
import math
from settings import *
from ray import Ray

class Raycaster:
    def __init__(self, player,map):
        self.rays = []
        self.colours = []
        self.player = player
        self.map = map 

    def castAllRays(self,screen):
        self.rays = []
        rayAngle = self.player.angle - FOV / 2
        biggest_ray = -float('inf')
        smallest_ray = float('inf')
        for i in range(NUM_RAYS):
            ray = Ray(rayAngle, self.player, self.map)
            ray.cast()
            self.rays.append(ray)

            if ray.distance > biggest_ray:
                biggest_ray = ray.distance
            if ray.distance < smallest_ray:
                smallest_ray = ray.distance

            rayAngle += FOV / NUM_RAYS
            #ray.render(screen)

            ratio = smallest_ray / biggest_ray
            self.cooloor = (ratio * ray.distance) 
            self.colours.append(self.cooloor)

        

    def render(self, screen):
        i = 0
        for ray in self.rays:
            #print(self.colours[i])
            proj_plane = (WIN_WIDTH / 2) / math.tan(FOV / 2)
            self.dist = ray.distance if ray.distance != float('inf') else 0.000001
            line_height = (TS * proj_plane) / (self.dist + 0.000001)

            draw_begin = (WIN_HEIGHT / 2) - (line_height / 2)
            h = max(0, int(line_height))
            y = max(0, int(draw_begin))

            pg.draw.rect(screen, (self.colours[i],self.colours[i],self.colours[i]), (i * RES, y, RES, h))

            i += 1
            ray.render(screen)