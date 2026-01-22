import math, pygame as pg
from player import Player
from mappy import Map
from settings import *

class Ghost_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 64
        self.colour = (255, 165, 0)
        self.speed = 1
        self.x = 14 * TS
        self.y = 3 * TS

    def render(self, screen):
        rect = pg.Rect(
            int(self.x) - TS,
            int(self.y) - TS,
            self.size,
            self.size
        )
        pg.draw.rect(screen, self.colour, rect)
    
    def movement(self):
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        player_pos = Player.x,Player.y
        self.x_directions = [-1,1]
        self.y_directions = [-1,1]
        self.ok = True
        map = Map()

        #wall above
        self.above_X = int((self.x + TS/2) //TS) - 1
        self.above_Y = int((self.y - TS/2)//TS) - 1
        self.wall_above = map.show_grid(self.above_X, self.above_Y)
        print(self.above_X,self.above_Y)
        print(self.wall_above)
        print("")

        #wall below
        self.below_X = int((self.x + TS/2) //TS) - 1
        self.below_Y = int((self.y - TS/2)//TS) - 1 + 2
        self.wall_below = map.show_grid(self.below_X, self.below_Y)
        print(self.below_X,self.below_Y)
        print(self.wall_below) 
        print("")

        #wall left
        self.left_X = int((self.x + TS/2) //TS) - 2
        self.left_Y = int((self.y - TS/2)//TS) 
        self.wall_left = map.show_grid(self.left_X, self.left_Y)
        print(self.left_X,self.left_Y)
        print(self.wall_left) 
        print("")

        #wall right
        self.right_X = int((self.x + TS/2) //TS) 
        self.right_Y = int((self.y - TS/2)//TS) 
        self.wall_right = map.show_grid(self.right_X, self.right_Y)
        print(self.right_X,self.right_Y)
        print(self.wall_right)

